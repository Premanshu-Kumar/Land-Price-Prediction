# 🏡 Land Price Prediction — Punjab Real Estate ML System

An end-to-end **Machine Learning project for predicting land prices in Punjab**, built with a production-oriented architecture covering data collection, preprocessing, model training, hyperparameter optimization, explainability, experiment tracking, API serving, and interactive dashboards.

> **Goal:** Use real-estate data and machine learning to generate useful land-price predictions through a reproducible and scalable ML workflow.

## ✨ Key Features

* 🏠 Punjab real-estate land price prediction
* 🧹 Data cleaning, preprocessing, and validation
* 🤖 Machine learning with **CatBoost** and Scikit-learn
* 🎯 Hyperparameter tuning with **Optuna**
* 🔍 Model explainability with **SHAP**
* 📊 Experiment tracking with **MLflow**
* ⚡ REST prediction API using **FastAPI**
* 📈 Interactive dashboard using **Streamlit + Plotly**
* 🌐 Modern web frontend using **React/Vite**
* 🕷️ Real-estate data collection using **Playwright + BeautifulSoup**
* 💾 SQLite-based local storage and tracking
* 🐳 Docker deployment support
* 🔐 API key configuration through environment variables
* 🧪 Automated testing and prediction verification

The repository includes Python utilities for data generation and prediction verification, along with installation, testing, and runtime helpers.

---

## 🧠 Project Architecture

```text
                    ┌──────────────────────┐
                    │   Real Estate Data   │
                    │  Collection / Input  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Cleaning & Validation │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Engineering  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Model Training    │
                    │ CatBoost / sklearn   │
                    └──────────┬───────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
             ┌──────────────┐    ┌──────────────┐
             │   FastAPI    │    │  Streamlit   │
             │     API      │    │  Dashboard   │
             └──────┬───────┘    └──────┬───────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Predictions &        │
                    │ Explainability       │
                    └──────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                        |
| ----------------- | ------------------------------ |
| **Python 3.11**   | Core development               |
| **Pandas**        | Data processing                |
| **Scikit-learn**  | Machine learning utilities     |
| **CatBoost**      | Gradient boosting model        |
| **Optuna**        | Hyperparameter optimization    |
| **FastAPI**       | Prediction API                 |
| **Uvicorn**       | API server                     |
| **Streamlit**     | Interactive dashboard          |
| **Plotly**        | Data visualization             |
| **SHAP**          | Model explainability           |
| **MLflow**        | Experiment tracking            |
| **Playwright**    | Web automation/data collection |
| **BeautifulSoup** | HTML parsing                   |
| **SQLite**        | Local database/tracking        |
| **Docker**        | Containerization               |
| **Pytest**        | Testing                        |

These dependencies are defined in the project's requirements, including FastAPI, Streamlit, Plotly, MLflow, SHAP, CatBoost, Optuna, Playwright, and testing/security tooling.

---

## 📁 Project Structure

```text
Land-Price-Prediction/
│
├── src/                    # Backend, ML and application source
├── models/                 # Trained model artifacts
├── data/                   # Raw and processed datasets
├── frontend/               # React/Vite frontend
├── dashboard/              # Streamlit dashboard
├── tests/                  # Automated tests
│
├── Dockerfile              # Docker deployment configuration
├── requirements.txt        # Python dependencies
├── INSTALL.md              # Installation instructions
├── generate_dummy_data.py  # Generate sample data
├── verify_prediction.py    # Prediction verification
├── run_project.ps1         # Launch all project components
├── .env.example            # Environment template
└── README.md
```

The repository also contains generated logs, local databases, MLflow tracking data, and other development artifacts.

---

## 🚀 Getting Started

### Prerequisites

Install:

* Python **3.11**
* Node.js + npm
* Git
* Docker — optional

The supplied installation guide specifically targets Python 3.11 and includes Playwright browser installation.

### 1. Clone the Repository

```bash
git clone https://github.com/Premanshu-Kumar/Land-Price-Prediction.git
cd Land-Price-Prediction
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Playwright

```bash
playwright install chromium
```

Or install all browsers:

```bash
playwright install
```

This follows the project's existing installation workflow.

---

## 🔐 Environment Configuration

Create your local environment file:

```bash
cp .env.example .env
```

Configure the required values inside `.env`.

Example:

```env
API_KEYS=your_api_key_here
```

The repository's environment template also supports inference database and MLflow configuration.

> ⚠️ **Never commit real API keys, passwords, or other secrets to GitHub.**

---

## ▶️ Running the Application

The project is designed as a multi-component application.

### ⚡ FastAPI Backend

```bash
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

API:

```text
http://localhost:8000
```

### 📊 Streamlit Dashboard

```bash
python -m streamlit run dashboard/app.py --server.port 8501
```

Dashboard:

```text
http://localhost:8501
```

### 🌐 React/Vite Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

The included PowerShell launcher starts these three components on ports **8000**, **8501**, and **5173** respectively.

---

## 🚀 Run Everything with PowerShell

The repository includes:

```text
run_project.ps1
```

Run:

```powershell
.\run_project.ps1
```

This starts:

```text
FastAPI Backend     → 8000
Streamlit Dashboard → 8501
React Frontend      → 5173
```

---

## 🐳 Docker Deployment

The project includes a production-oriented Dockerfile based on **Python 3.11-slim**.

It installs the required system dependencies, copies the source code and model artifacts, and starts the FastAPI inference service on port **8000**.

### Build

```bash
docker build -t land-price-prediction .
```

### Run

```bash
docker run --rm \
  -p 8000:8000 \
  --env-file .env \
  land-price-prediction
```

---

## 🧠 Machine Learning Workflow

```text
Real Estate Data
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Validation
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Hyperparameter Optimization
       ↓
Model Evaluation
       ↓
Model Artifact / Registry
       ↓
Prediction API
       ↓
Dashboard / Frontend
       ↓
Explainability
```

---

## 🤖 Machine Learning

### CatBoost

The project includes **CatBoost** as a gradient-boosting model for the prediction workflow.

### Optuna

**Optuna** is included for automated hyperparameter optimization, helping search for better model configurations.

Both technologies are included in the project's dependency configuration.

---

## 🔍 Model Explainability

The project uses **SHAP (SHapley Additive Explanations)** to make model predictions more interpretable.

This can help answer questions such as:

> Which features are contributing most to a predicted land price?

SHAP is included directly in the project's ML stack.

---

## 📊 Experiment Tracking

**MLflow** is included for tracking experiments and model-development information.

The project also provides SQLite-based tracking support for local development.

---

## 🌐 Application Interfaces

### FastAPI

The API provides a production-style inference layer for serving predictions.

### Streamlit

The Streamlit dashboard provides an interactive interface for analytics and model interaction.

### React + Vite

The frontend provides a modern web interface for interacting with the backend.

This multi-interface structure is reflected in the project's launcher configuration.

---

## 🕷️ Data Collection

The project includes browser automation and web-parsing tools:

```text
Playwright
BeautifulSoup
lxml
fake-useragent
```

These tools support real-estate data collection and parsing workflows.

---

## 🧪 Testing

The repository includes testing and prediction-verification utilities.

Run the test suite:

```bash
pytest
```

Run prediction verification:

```bash
python verify_prediction.py
```

The dependency stack also includes Pandera, HTTPX, Locust, Ruff, and pip-audit for validation, API testing, load testing, code quality, and dependency security auditing.

---

## 📈 Example Use Case

A user provides real-estate information such as property characteristics and location-related attributes.

The system then:

```text
Input Property Information
          ↓
Preprocessing
          ↓
Trained ML Model
          ↓
Predicted Land Price
          ↓
Explain Prediction
```

The prediction can then be exposed through the API or presented through the dashboard/frontend.

---

## 🔮 Future Improvements

* Improve prediction accuracy with richer locality and geographic features
* Add map-based property visualization
* Add additional regression models for benchmarking
* Introduce automated model retraining
* Add model drift monitoring
* Add CI/CD pipelines
* Improve cloud deployment
* Add real-time market-data integration
* Improve frontend UX and mobile responsiveness

---

## 👨‍💻 Author

**Premanshu Kumar**

GitHub: [@Premanshu-Kumar](https://github.com/Premanshu-Kumar)

Project: [Land Price Prediction](https://github.com/Premanshu-Kumar/Land-Price-Prediction)

---

## ⭐ Support

If you find this project useful for **Machine Learning, Data Science, or Real Estate Analytics**, consider giving the repository a ⭐ star.

---

Made with  using **Python • Machine Learning • FastAPI • Streamlit • React**
