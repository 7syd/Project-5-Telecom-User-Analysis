import pandas as pd

from src.features import (
    build_engagement_features,
    build_experience_features,
    build_feature_store
)


def create_test_data():
    return pd.DataFrame({
        "MSISDN/Number": [1, 1, 2],
        "Dur. (ms)": [1000, 2000, 3000],
        "Total DL (Bytes)": [100, 200, 300],
        "Total UL (Bytes)": [50, 50, 100],
        "TCP DL Retrans. Vol (Bytes)": [10, 20, 30],
        "TCP UL Retrans. Vol (Bytes)": [5, 10, 15],
        "Avg RTT DL (ms)": [20, 30, 40],
        "Avg RTT UL (ms)": [5, 10, 15],
        "Avg Bearer TP DL (kbps)": [100, 200, 300],
        "Avg Bearer TP UL (kbps)": [50, 100, 150]
    })


def test_engagement_features():
    df = create_test_data()

    result = build_engagement_features(df)

    assert len(result) == 2
    assert result.loc[
        result["MSISDN/Number"] == 1,
        "Number_of_Sessions"
    ].iloc[0] == 2


def test_experience_features():
    df = create_test_data()

    result = build_experience_features(df)

    assert len(result) == 2
    assert "Avg_RTT_DL" in result.columns
    assert "Avg_Throughput_DL" in result.columns


def test_feature_store():
    df = create_test_data()

    result = build_feature_store(df)

    assert len(result) == 2
    assert result["MSISDN/Number"].is_unique
    assert "Total_Traffic_Bytes" in result.columns
    assert "Avg_TCP_DL_Retrans" in result.columns
