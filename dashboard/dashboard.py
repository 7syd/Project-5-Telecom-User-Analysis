import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Telecom User Analytics",
    page_icon="📡",
    layout="wide"
)

# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("dashboard/customer_dashboard.csv")


df = load_data()

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("📡 Telecom User Analytics")
st.markdown(
    "### Customer Engagement, Network Experience & Satisfaction"
)

st.divider()

# ---------------------------------------------------------
# KPI calculations
# ---------------------------------------------------------

total_customers = df["MSISDN/Number"].nunique()
total_sessions = df["Number_of_Sessions"].sum()

avg_experience = df["Experience_Score"].mean()
avg_satisfaction = df["Satisfaction_Score"].mean()

# ---------------------------------------------------------
# KPI cards
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with col2:
    st.metric(
        "📊 Total Sessions",
        f"{total_sessions:,}"
    )

with col3:
    st.metric(
        "📶 Avg Experience Score",
        f"{avg_experience:.3f}"
    )

with col4:
    st.metric(
        "⭐ Avg Satisfaction Score",
        f"{avg_satisfaction:.3f}"
    )

st.divider()

# ---------------------------------------------------------
# Basic dataset information
# ---------------------------------------------------------

st.subheader("Dataset Overview")

st.write(
    f"The dashboard contains **{total_customers:,} customers** "
    f"across **{len(df.columns)} customer-level features**."
)

# ---------------------------------------------------------
# Engagement & Experience
# ---------------------------------------------------------

st.header("📊 Engagement & Experience")

col1, col2 = st.columns(2)

with col1:
    engagement_counts = (
        df["Engagement_Level"]
        .value_counts()
        .reset_index()
    )
    engagement_counts.columns = ["Engagement Level", "Customers"]

    fig = px.bar(
        engagement_counts,
        x="Engagement Level",
        y="Customers",
        title="Customer Engagement Distribution",
        text="Customers"
    )

    fig.update_layout(
        xaxis_title="Engagement Level",
        yaxis_title="Customers",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


with col2:
    experience_counts = (
        df["Experience_Level"]
        .value_counts()
        .reset_index()
    )
    experience_counts.columns = ["Experience Level", "Customers"]

    fig = px.bar(
        experience_counts,
        x="Experience Level",
        y="Customers",
        title="Customer Experience Distribution",
        text="Customers"
    )

    fig.update_layout(
        xaxis_title="Experience Level",
        yaxis_title="Customers",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)