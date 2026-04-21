import joblib
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from pathlib import Path
import json

MODELS_DIR = Path("models")

def load_models():
    cb_model = CatBoostRegressor()
    cb_model.load_model(str(MODELS_DIR / "catboost_model.cbm"))
    meta_model = joblib.load(MODELS_DIR / "meta_model.joblib")
    scaler = joblib.load(MODELS_DIR / "scaler.joblib")
    ohe = joblib.load(MODELS_DIR / "ohe.joblib")
    with open(MODELS_DIR / "locality_stats.json", "r") as f:
        stats = json.load(f)
    return cb_model, meta_model, scaler, ohe, stats

def predict(area_sqft, bedrooms, bathrooms, city, locality, age_bucket):
    cb_model, meta_model, scaler, ohe, stats = load_models()
    
    # 1. Historical Features
    loc_map = stats["locality_median_ppsf"]
    city_map = stats["city_median_ppsf"]
    global_med = stats["global_median_ppsf"]
    locality_historical_ppsf = loc_map.get(locality, city_map.get(city, global_med))
    
    locality_median_ppsf_90d = stats["locality_median_ppsf_90d"].get(locality, global_med)
    city_ppsf_trend_30d = stats["city_ppsf_trend_30d"].get(city, 0)
    
    # 2. Engineered Features
    bhk_density = bedrooms / area_sqft
    from src.engine.features import is_premium_locality, parse_age_to_bucket
    is_premium = is_premium_locality(locality)
    mapped_age_bucket = parse_age_to_bucket(age_bucket)
    
    # Numerical
    # ["area_sqft", "bedrooms", "bathrooms", "bhk_density", "locality_historical_ppsf", "luxury_score", "locality_median_ppsf_90d", "city_ppsf_trend_30d"]
    # Trainer.py has luxury_score in NUMERICAL_FEATURES
    from src.engine.features import compute_luxury_score
    luxury_score = compute_luxury_score(is_premium, mapped_age_bucket)
    
    num_features = [
        area_sqft, bedrooms, bathrooms, bhk_density,
        locality_historical_ppsf, luxury_score,
        locality_median_ppsf_90d, city_ppsf_trend_30d
    ]
    
    # Categorical
    # ["age_bucket", "city", "locality", "is_premium_locality"]
    cat_features = [mapped_age_bucket, city, locality, is_premium]
    
    # CatBoost Prediction
    cb_input = pd.DataFrame([num_features + cat_features], columns=[
        "area_sqft", "bedrooms", "bathrooms", "bhk_density",
        "locality_historical_ppsf", "luxury_score",
        "locality_median_ppsf_90d", "city_ppsf_trend_30d",
        "age_bucket", "city", "locality", "is_premium_locality"
    ])
    cb_log_ppsf = cb_model.predict(cb_input)[0]
    
    # MLX Prediction (Skip for simplicity or assume 0 if not available)
    mlx_log_ppsf = 0 
    
    # Meta Model
    meta_X = np.column_stack([[cb_log_ppsf], [mlx_log_ppsf]])
    final_log_ppsf = meta_model.predict(meta_X)[0]
    final_ppsf = np.expm1(final_log_ppsf)
    final_price = final_ppsf * area_sqft
    
    return final_price

if __name__ == "__main__":
    # Test with a realistic sample
    test_cases = [
        {"area_sqft": 1000, "bedrooms": 2, "bathrooms": 2, "city": "Ludhiana", "locality": "Model Town", "age_bucket": "0-1 years"},
        {"area_sqft": 2000, "bedrooms": 3, "bathrooms": 3, "city": "Chandigarh", "locality": "Sector 62", "age_bucket": "New Launch"},
        {"area_sqft": 3000, "bedrooms": 4, "bathrooms": 4, "city": "Mohali", "locality": "Aerocity", "age_bucket": "1-3 years"},
    ]
    
    for case in test_cases:
        price = predict(**case)
        print(f"Case: {case}")
        print(f"Predicted Price: ₹{price:,.0f}")
        print("-" * 20)
