import os
import sqlite3
import numpy as np
import pandas as pd
from pathlib import Path

# Part 1: Global Synthetic Data Ban
if not os.getenv("PYTEST_CURRENT_TEST"):
    raise RuntimeError(
        "Synthetic data generation is strictly forbidden outside test environments. "
        "Use src/scraper/seed_database.py for baseline data."
    )

db_path = Path("data/raw/punjab_real_estate.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

np.random.seed(42)
n_rows = 500
cities = ["Ludhiana", "Mohali", "Chandigarh"]
localities = ["Model Town", "Phase 7 Mohali", "Sarabha Nagar", "Sector 62", "Aerocity"]

data = {
    "city": [cities[i % len(cities)] for i in range(n_rows)],
    "locality": [localities[i % len(localities)] for i in range(n_rows)],
    "price": np.random.uniform(1_000_000, 50_000_000, n_rows),
    "area_sqft": np.random.uniform(500, 5000, n_rows),
    "bedrooms": np.random.randint(1, 6, n_rows),
    "bathrooms": np.random.randint(1, 5, n_rows),
    "property_age": ["5 years old" if i % 2 == 0 else "New Launch" for i in range(n_rows)],
    "scraped_at": ["2026-03-09"] * n_rows
}
df_synthetic = pd.DataFrame(data)

conn = sqlite3.connect(db_path)
df_synthetic.to_sql("raw_listings", conn, index=False, if_exists="replace")
conn.close()
print(f"Populated {db_path} with {n_rows} synthetic listings.")
