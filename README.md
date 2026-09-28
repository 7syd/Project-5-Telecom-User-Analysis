# 📡 Telecom User Analytics

> **End-to-end customer analytics and machine learning pipeline for a telecommunications dataset.**

This project analyzes telecom customer behavior across **engagement, network experience, and satisfaction**. It combines exploratory data analysis, customer segmentation, feature engineering, machine learning, MySQL, MLflow, FastAPI, Docker, unit testing, and CI/CD into a reusable analytics pipeline.

---

## 📌 Project Overview

The goal of this project is to understand how customers use a telecommunications network, evaluate their network experience, and derive an overall satisfaction score.

The analysis is divided into four major areas:

| Area | Focus |
|---|---|
| 👤 **User Overview** | Handsets, manufacturers, usage patterns |
| 📊 **User Engagement** | Sessions, duration, and traffic |
| 📶 **User Experience** | TCP retransmission, RTT, and throughput |
| ⭐ **User Satisfaction** | Combined engagement and experience analysis |

The final dataset contains **148,506 records and 55 columns**, representing **106,856 unique customers** after preprocessing.

---

## 🔄 Project Workflow

```text
Raw Telecom Data
       │
       ▼
Data Cleaning & Preparation
       │
       ▼
Exploratory Data Analysis
       │
       ├───────────────┐
       ▼               ▼
User Engagement    User Experience
       │               │
       ▼               ▼
K-Means Clustering   K-Means Clustering
       │               │
       └───────┬───────┘
               ▼
       Satisfaction Scoring
               │
               ▼
      Regression Modeling
               │
               ▼
    Satisfaction Clustering
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
      MySQL   MLflow  FastAPI
                       │
                       ▼
                     Docker
```

---

## 👤 User Overview

The user overview analysis examined:

- Top 10 handset types
- Top 3 handset manufacturers
- Top 5 handsets for each major manufacturer
- Customer-level usage statistics
- Missing values and outliers
- Univariate and bivariate relationships
- Application traffic compared with total traffic
- Traffic distribution using deciles

### 📱 Most Represented Manufacturers

The three most represented manufacturers were:

- **Apple**
- **Samsung**
- **Huawei**

The analysis also identified the most frequently used handset models for each manufacturer.

---

## 📊 User Engagement Analytics

Customer-level engagement features were created using:

- Number of sessions
- Total session duration
- Total download traffic
- Total upload traffic
- Total traffic

### Engagement Segmentation

K-Means clustering with **K = 3** was used to segment customers into engagement groups.

| Segment | Customers | Description |
|---|---:|---|
| 🟢 Low Engagement | 81,163 | Lower sessions, duration and traffic |
| 🟡 Medium Engagement | 21,645 | Moderate usage |
| 🔵 High Engagement | 4,048 | Higher sessions, duration and traffic |

The clustering showed that the majority of customers belonged to the low-engagement segment, while a smaller group demonstrated substantially higher usage.

---

## 📶 User Experience Analytics

Network experience was evaluated using:

### TCP Retransmission
- TCP DL retransmission
- TCP UL retransmission

### RTT
- Average RTT DL
- Average RTT UL

### Throughput
- Average throughput DL
- Average throughput UL

Missing values and extreme observations were handled before customer-level experience scoring and clustering.

### Experience Segmentation

K-Means clustering with **K = 3** was applied to the six experience metrics.

The resulting groups represented relatively different network experience profiles based on:

- Retransmission
- Latency
- Download throughput
- Upload throughput

Handset-level analysis was also performed to examine differences in throughput and retransmission across devices.

---

## ⭐ Customer Satisfaction

Customer satisfaction was derived by combining engagement and experience.

### Engagement Score

The engagement score was calculated as the Euclidean distance between each customer's normalized engagement profile and the **less-engaged cluster center**.

### Experience Score

The experience score was calculated as the Euclidean distance between each customer's normalized experience profile and the **worst-experience cluster center**.

### Satisfaction Score

The final satisfaction score was calculated as:

```text
Satisfaction Score
    = (Engagement Score + Experience Score) / 2
```

The resulting scores were used for further modeling and customer segmentation.

---

## 🤖 Satisfaction Prediction

A Linear Regression model was trained using the engagement and experience features.

### Model Performance

| Metric | Result |
|---|---:|
| RMSE | **0.0351** |
| R² | **0.8194** |

The model was trained using an **80/20 train-test split** with `random_state=42`.

> Note: The satisfaction score is derived from the underlying engagement and experience scores, so the regression task is primarily a demonstration of the modeling pipeline rather than an independent real-world target.

---

## 🧩 Satisfaction Segmentation

A second K-Means model with **K = 2** was applied using engagement and experience scores.

| Cluster | Customers | Avg. Satisfaction | Avg. Experience | Avg. Engagement |
|---|---:|---:|---:|---:|
| Cluster 0 | 86,022 | 0.4857 | 0.9257 | 0.0456 |
| Cluster 1 | 20,834 | 0.3322 | 0.5908 | 0.0736 |

This provides a final customer segmentation based on the combined engagement and experience dimensions.

---

## 🗄️ MySQL Integration

The final customer-level scores were exported to a local MySQL database.

### Database

```text
Database: telecom_analysis
Table: customer_scores
```

### Stored fields

```text
MSISDN_Number
Engagement_Score
Experience_Score
Satisfaction_Score
```

A total of **106,856 customer records** were inserted and validated using SQL queries.

---

## 📈 MLflow Experiment Tracking

MLflow was used to track the satisfaction regression experiment.

Tracked information includes:

- Model parameters
- RMSE
- R²
- Trained regression model

The trained model was saved as:

```text
models/satisfaction_regression_model.pkl
```

---

## 🚀 FastAPI Deployment

A FastAPI application was created to expose the trained model through an API.

### Endpoints

```text
GET /
```

Health/status endpoint.

```text
POST /predict
```

Accepts customer feature values and returns a predicted satisfaction score.

Example response:

```json
{
  "predicted_satisfaction_score": 1.0887824951614828
}
```

---

## 🐳 Docker

The FastAPI application was containerized using Docker.

The Docker image:

```text
telecom-satisfaction-api:latest
```

The container exposes the API on:

```text
http://localhost:8000
```

The Dockerized API was tested successfully using the `/predict` endpoint.

---

## 🧪 Testing

Unit tests were created for the reusable feature-engineering functions.

The test suite covers:

- Engagement feature generation
- Experience feature generation
- Combined feature store generation

Current result:

```text
3 tests passed
```

Run the tests with:

```bash
python -m pytest
```

---

## ⚙️ CI/CD

GitHub Actions is configured to automatically run the test suite on:

- Push
- Pull request

Workflow:

```text
.github/workflows/tests.yml
```

The workflow:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies
4. Runs the pytest suite

---

## 🧱 Reusable Feature Engineering

Reusable feature-engineering functions are located in:

```text
src/features.py
```

The module provides:

```python
build_engagement_features()
build_experience_features()
build_feature_store()
```

The resulting customer-level feature store is saved at:

```text
feature_store/customer_features.csv
```

---

## 📁 Project Structure

```text
telecom-user-analytics/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── app/
│   └── app.py
│
├── feature_store/
│   └── customer_features.csv
│
├── models/
│   └── satisfaction_regression_model.pkl
│
├── notebooks/
│   └── telecom_analysis.ipynb
│
├── src/
│   └── features.py
│
├── tests/
│   └── test_features.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## 🛠️ Tech Stack

### Data & Analysis
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### Machine Learning
- K-Means Clustering
- Linear Regression
- Feature Scaling
- Euclidean Distance

### Database
- MySQL
- MySQL Connector/Python

### MLOps & Deployment
- MLflow
- FastAPI
- Docker

### Testing & CI/CD
- Pytest
- GitHub Actions

---

## 📌 Key Deliverables

- ✅ Telecom data preprocessing
- ✅ Exploratory data analysis
- ✅ Customer engagement analysis
- ✅ Customer experience analysis
- ✅ Engagement clustering
- ✅ Experience clustering
- ✅ Customer satisfaction scoring
- ✅ Satisfaction prediction model
- ✅ Satisfaction clustering
- ✅ MySQL integration
- ✅ MLflow experiment tracking
- ✅ Reusable feature-engineering module
- ✅ Feature store
- ✅ FastAPI prediction API
- ✅ Docker deployment
- ✅ Unit tests
- ✅ GitHub Actions CI/CD

---

## 👨‍💻 Author

**Siddheya**

B.E. Artificial Intelligence & Data Science

---

> **Built as an end-to-end data analytics and machine learning project covering the complete path from raw telecom data to a deployed prediction API.**
