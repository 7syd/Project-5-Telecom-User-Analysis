\# Telecom User Analytics



A machine learning and analytics project for analyzing customer engagement, network experience, and satisfaction in the telecommunications industry.



\## Project Overview



This project analyzes telecom customer data to understand:



\- User engagement and activity

\- Network experience and performance

\- Customer satisfaction

\- Customer segmentation

\- Satisfaction prediction

\- Model tracking and deployment



The project follows a complete analytics-to-deployment workflow, including data preprocessing, exploratory data analysis, feature engineering, clustering, regression, MySQL integration, MLflow tracking, API deployment, Docker, reusable feature engineering, automated testing, and CI/CD.



\## Objectives



The project focuses on four major areas:



1\. \*\*User Overview\*\*

2\. \*\*User Engagement Analysis\*\*

3\. \*\*User Experience Analysis\*\*

4\. \*\*User Satisfaction Analysis\*\*



\---



\## Dataset



The telecom dataset contains customer session-level information including:



\- Customer identifiers

\- Session duration

\- Download and upload traffic

\- TCP retransmission

\- RTT

\- Throughput

\- Handset manufacturer

\- Handset type

\- Application traffic



After data preparation and cleaning, the final dataset contained:



\*\*148,506 records and 55 columns\*\*



The customer-level feature store contains approximately:



\*\*106,856 unique customers\*\*



\---



\## Project Workflow



```text

Raw Telecom Data

&#x20;      │

&#x20;      ▼

Data Cleaning \& Preparation

&#x20;      │

&#x20;      ▼

Exploratory Data Analysis

&#x20;      │

&#x20;      ├───────────────┐

&#x20;      ▼               ▼

Engagement        Experience

Analysis          Analysis

&#x20;      │               │

&#x20;      └───────┬───────┘

&#x20;              ▼

&#x20;       Customer Features

&#x20;              │

&#x20;              ▼

&#x20;     Customer Satisfaction

&#x20;              │

&#x20;      ┌───────┴────────┐

&#x20;      ▼                ▼

&#x20;  Clustering       Regression

&#x20;      │                │

&#x20;      └───────┬────────┘

&#x20;              ▼

&#x20;       Model Tracking

&#x20;           MLflow

&#x20;              │

&#x20;              ▼

&#x20;         FastAPI API

&#x20;              │

&#x20;              ▼

&#x20;           Docker

```



\## User Overview



The user overview analysis included:



\- Top handset manufacturers

\- Most-used handsets

\- Top handsets for major manufacturers

\- Missing-value analysis

\- Outlier analysis

\- Univariate analysis

\- Bivariate analysis

\- Correlation analysis



The three most represented handset manufacturers were:



\- Apple

\- Samsung

\- Huawei



Huawei B528S-23A was particularly prominent in the dataset and represents a network/router-type device rather than a conventional smartphone.



\---



\## User Engagement Analysis



Customer-level engagement features were created using:



\- Number of sessions

\- Total session duration

\- Total download traffic

\- Total upload traffic

\- Total traffic



K-Means clustering with \*\*3 clusters\*\* was used to segment customers into:



\- Low Engagement

\- Medium Engagement

\- High Engagement



The resulting customer distribution was approximately:



| Segment | Users | Percentage |

|---|---:|---:|

| Low Engagement | 81,163 | 75.9% |

| Medium Engagement | 21,645 | 20.3% |

| High Engagement | 4,048 | 3.8% |



\---



\## User Experience Analysis



Experience was analyzed using:



\- TCP downlink retransmission

\- TCP uplink retransmission

\- Downlink RTT

\- Uplink RTT

\- Downlink throughput

\- Uplink throughput



The metrics showed strong skewness and extreme values, particularly for TCP retransmission and RTT.



K-Means clustering with \*\*3 clusters\*\* was used to identify customer experience segments.



The clusters were interpreted as:



\- Low Experience

\- Medium Experience

\- High Experience



The high-experience cluster showed stronger throughput performance across both download and upload metrics.



\---



\## Customer Satisfaction



Customer satisfaction was calculated from two components:



\### Engagement Score



The engagement score represents the Euclidean distance between each customer's engagement feature vector and the less-engaged cluster center.



\### Experience Score



The experience score represents the Euclidean distance between each customer's experience feature vector and the worst-experience cluster center.



The final satisfaction score was calculated as:



```text

Satisfaction Score =

(Engagement Score + Experience Score) / 2

```



The resulting satisfaction dataset contained:



\*\*106,856 customers\*\*



\---



\## Satisfaction Prediction



A Linear Regression model was trained to predict the satisfaction score using nine engineered features:



\- Sessions Score

\- Duration Score

\- Traffic Score

\- TCP DL Score

\- TCP UL Score

\- RTT DL Score

\- RTT UL Score

\- Throughput DL Score

\- Throughput UL Score



\### Model Performance



| Metric | Result |

|---|---:|

| RMSE | 0.0351 |

| R² | 0.8194 |



The model achieved an R² of approximately \*\*0.819\*\*, meaning it explained about 81.9% of the variation in the test-set satisfaction scores.



\---



\## Satisfaction Clustering



A second K-Means model with \*\*2 clusters\*\* was applied to the engagement and experience scores.



The resulting groups showed different combinations of engagement and experience characteristics.



The larger cluster had:



\- Average satisfaction: \*\*0.4857\*\*

\- Average experience: \*\*0.9257\*\*

\- Average engagement: \*\*0.0456\*\*



The smaller cluster had:



\- Average satisfaction: \*\*0.3322\*\*

\- Average experience: \*\*0.5908\*\*

\- Average engagement: \*\*0.0736\*\*



\---



\## MySQL Integration



The final customer scores were exported to a local MySQL database.



Database:



```text

telecom\_analysis

```



Table:



```text

customer\_scores

```



The table contains:



\- Customer ID

\- Engagement Score

\- Experience Score

\- Satisfaction Score



A SQL query was used to verify the stored customer records.



\---



\## MLflow



ML

