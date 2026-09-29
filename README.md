# 📡 Telecom User Analytics

A complete customer analytics project for the telecommunications industry, covering **user overview, engagement, experience, satisfaction, machine learning, dashboarding, API deployment, feature engineering, testing, and MLOps**.

---

## 📌 Project Overview

This project analyzes telecom customer data to understand:

- Who the customers are and which handsets they use
- How customers engage with telecom services
- The quality of their network experience
- Overall customer satisfaction
- Customer segmentation using clustering
- Satisfaction prediction using machine learning

The project also includes a reusable feature store, Streamlit dashboard, REST API, MySQL database integration, MLflow experiment tracking, Docker deployment, unit tests, and CI/CD.

---

## 🎯 Project Objectives

The analysis is divided into four major areas:

1. **User Overview**
2. **User Engagement Analysis**
3. **User Experience Analysis**
4. **Customer Satisfaction Analysis**

---

## 📊 Dataset

The telecom dataset contains:

- **148,506 records**
- **55 columns**
- **106,856 unique customers**

The dataset contains information related to:

- Customer sessions
- Session duration
- Download and upload traffic
- TCP retransmission
- RTT
- Network throughput
- Handset manufacturer and type
- Application-level traffic

---

# 🔎 Analysis Workflow

## 1. Data Cleaning & Preparation

The raw telecom dataset was cleaned and prepared for analysis.

Steps included:

- Handling missing values
- Identifying highly incomplete variables
- Removing redundant variables
- Detecting outliers using the IQR method
- Checking variable and data types
- Preparing numerical and categorical variables
- Creating a cleaned analytical dataset

Final cleaned dataset:

**148,506 rows × 55 columns**

---

# 👤 2. User Overview Analysis

The user overview analysis investigated customer and handset characteristics.

### Handset Analysis

The analysis identified:

- Top 10 most frequently used handsets
- Top 3 handset manufacturers
- Top 5 handsets for each of the top 3 manufacturers

### Customer-Level Aggregation

Customer-level features were created for:

- Number of sessions
- Total session duration
- Total download traffic
- Total upload traffic
- Total traffic

---

# 📈 3. User Engagement Analysis

Customer engagement was analyzed using:

- Number of sessions
- Total session duration
- Total traffic

Customers were normalized and segmented using **K-Means clustering with K=3**.

### Engagement Segments

| Segment | Description |
|---|---|
| Low Engagement | Customers with relatively low activity |
| Medium Engagement | Customers with moderate activity |
| High Engagement | Customers with relatively high activity |

The engagement analysis was then used as one of the inputs for the customer satisfaction analysis.

---

# 📶 4. User Experience Analysis

Network experience was evaluated using:

- TCP Downlink Retransmission
- TCP Uplink Retransmission
- Downlink RTT
- Uplink RTT
- Downlink Throughput
- Uplink Throughput

Missing values and extreme values were handled before customer-level experience scoring.

K-Means clustering with **K=3** was used to identify different experience groups.

### Experience Segments

| Segment | Description |
|---|---|
| Low Experience | Relatively poorer network experience |
| Medium Experience | Moderate network experience |
| High Experience | Relatively better network experience |

Handset-level analysis was also performed to investigate differences in:

- Average throughput
- TCP retransmission

---

# ⭐ 5. Customer Satisfaction Analysis

Customer satisfaction was calculated by combining engagement and experience scores.

### Satisfaction Formula

```text
Satisfaction Score =
(Engagement Score + Experience Score) / 2
```

The analysis included:

- Engagement score calculation
- Experience score calculation
- Customer satisfaction scoring
- Top 10 most satisfied customers
- Satisfaction prediction
- Satisfaction clustering

---

# 🤖 Machine Learning

## Satisfaction Prediction

A **Linear Regression** model was trained to predict customer satisfaction.

### Model Performance

| Metric | Result |
|---|---:|
| RMSE | 0.0351 |
| R² | 0.8194 |

The model was trained using engagement and experience-related customer features.

---

## Customer Satisfaction Clustering

K-Means clustering with **K=2** was applied using engagement and experience scores.

This produced two customer groups representing different satisfaction profiles.

---

# 📊 Streamlit Dashboard

A web-based dashboard was developed using **Streamlit**.

The dashboard provides an interactive overview of:

- Total customers
- Total sessions
- Average experience score
- Average satisfaction score
- Customer engagement distribution
- Customer experience distribution
- Customer satisfaction
- Customer-level analytics

### Run the Dashboard

From the project root:

```bash
python -m streamlit run dashboard/dashboard.py
```

The dashboard uses the customer-level dataset:

```text
dashboard/customer_dashboard.csv
```

---

# 🗄️ MySQL Integration

The final customer scoring data was exported to a local MySQL database.

### Database

```text
telecom_analysis
```

### Table

```text
customer_scores
```

The table contains:

- Customer ID
- Engagement Score
- Experience Score
- Satisfaction Score

A SQL query was used to verify the stored customer scores.

---

# 📈 MLflow Experiment Tracking

**MLflow** was used to track the satisfaction regression experiment.

Tracked information included:

- Model parameters
- RMSE
- R²
- Trained regression model

Experiment:

```text
Telecom Customer Satisfaction
```

---

# 🧩 Reusable Feature Engineering

Reusable feature engineering functions were created in:

```text
src/features.py
```

The module generates:

- Engagement features
- Experience features
- Combined customer-level feature store

This allows the feature engineering process to be reused without rewriting the analysis code.

---

# 🗃️ Feature Store

A customer-level feature store was generated containing the aggregated engagement and experience features.

Location:

```text
feature_store/customer_features.csv
```

The feature store contains customer-level analytical features that can be reused by downstream models and applications.

---

# 🌐 REST API

A **FastAPI** application was created to serve the trained satisfaction model.

### API Endpoint

```text
POST /predict
```

The API accepts customer feature values and returns a predicted satisfaction score.

### Run Locally

```bash
uvicorn app.app:app --reload
```

---

# 🐳 Docker Deployment

The FastAPI application was containerized using Docker.

Build the image:

```bash
docker build -t telecom-satisfaction-api .
```

Run the container:

```bash
docker run -p 8000:8000 telecom-satisfaction-api
```

The API can then be accessed locally through port `8000`.

---

# 🧪 Unit Testing

Unit tests were created using **pytest** to verify the reusable feature engineering functions.

Tests cover:

- Engagement feature generation
- Experience feature generation
- Combined feature store generation

Run tests:

```bash
python -m pytest
```

Current test suite:

**3 tests passed**

---

# ⚙️ CI/CD

GitHub Actions is configured to automatically run the test suite when changes are pushed or pull requests are created.

Workflow:

```text
.github/workflows/tests.yml
```

The workflow:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Runs pytest

---

# 📁 Project Structure

```text
telecom-user-analytics/
│
├── app/
│   └── app.py
│
├── dashboard/
│   ├── dashboard.py
│   └── customer_dashboard.csv
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
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

### Programming & Analysis
- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy

### Visualization
- Matplotlib
- Seaborn
- Plotly
- Streamlit

### Machine Learning
- K-Means Clustering
- Linear Regression

### Database
- MySQL
- mysql-connector-python

### MLOps & Deployment
- MLflow
- FastAPI
- Docker
- Uvicorn

### Testing & CI/CD
- Pytest
- GitHub Actions

---

# 📌 Key Project Components

| Component | Implementation |
|---|---|
| Data Cleaning | Pandas |
| User Overview | Python / Pandas |
| Engagement Analysis | K-Means |
| Experience Analysis | K-Means |
| Satisfaction Analysis | Scoring + K-Means |
| Satisfaction Prediction | Linear Regression |
| Dashboard | Streamlit |
| Database | MySQL |
| Experiment Tracking | MLflow |
| API | FastAPI |
| Deployment | Docker |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Feature Engineering | Reusable Python module |
| Feature Store | Customer-level CSV |

---

## 🚀 Project Outcome

This project demonstrates an end-to-end telecom customer analytics workflow, starting from raw data preparation and exploratory analysis through **customer segmentation, satisfaction modeling, dashboarding, database storage, API deployment, testing, and MLOps practices**.

The project is designed so that the analytical features can be reused for future customer analytics and machine learning workflows.
