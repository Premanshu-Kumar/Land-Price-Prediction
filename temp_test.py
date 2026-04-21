import httpx
import json

API_URL = "http://localhost:8000"
HEADERS = {"x-api-key": "development_key", "Content-Type": "application/json"}

tests = [
    ("TEST 1: Normal Prediction - 3BHK in Model Town, Ludhiana (1200 sqft)",
     {"city": "Ludhiana", "locality": "Model Town", "bedrooms": 3, "bathrooms": 2, "sqft": 1200.0, "property_age": "5 years old"}),
    ("TEST 2: Premium Locality - 4BHK in Sarabha Nagar, Ludhiana (2500 sqft)",
     {"city": "Ludhiana", "locality": "Sarabha Nagar", "bedrooms": 4, "bathrooms": 3, "sqft": 2500.0, "property_age": "New Launch"}),
    ("TEST 3: Budget Property - 2BHK in Dugri, Ludhiana (800 sqft)",
     {"city": "Ludhiana", "locality": "Dugri", "bedrooms": 2, "bathrooms": 1, "sqft": 800.0, "property_age": "10+ years"}),
    ("TEST 4: Mohali Property - 3BHK in Phase 7 Mohali (1500 sqft)",
     {"city": "Mohali", "locality": "Phase 7 Mohali", "bedrooms": 3, "bathrooms": 2, "sqft": 1500.0, "property_age": "new"}),
    ("TEST 5: Extreme Property - 10BHK, 9999 sqft (OOD Test)",
     {"city": "Ludhiana", "locality": "Model Town", "bedrooms": 10, "bathrooms": 10, "sqft": 9999.0, "property_age": "10+ years"}),
]

with httpx.Client(timeout=30.0) as client:
    for title, payload in tests:
        print("=" * 70)
        print(title)
        print("=" * 70)
        try:
            r = client.post(f"{API_URL}/predict", json=payload, headers=HEADERS)
            print(f"Status: {r.status_code}")
            print(json.dumps(r.json(), indent=2))
        except Exception as e:
            print(f"ERROR: {e}")
        print()

    # Security tests
    print("=" * 70)
    print("TEST 6: Security Test - Invalid API Key")
    print("=" * 70)
    try:
        r = client.post(f"{API_URL}/predict", json=tests[0][1], headers={"x-api-key": "invalid_key"})
        print(f"Status: {r.status_code}")
        print(json.dumps(r.json(), indent=2))
    except Exception as e:
        print(f"ERROR: {e}")

    print()
    print("=" * 70)
    print("TEST 7: Security Test - Missing API Key")
    print("=" * 70)
    try:
        r = client.post(f"{API_URL}/predict", json=tests[0][1])
        print(f"Status: {r.status_code}")
        print(json.dumps(r.json(), indent=2))
    except Exception as e:
        print(f"ERROR: {e}")
