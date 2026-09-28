import pandas as pd


def build_engagement_features(df):
    """
    Create customer-level engagement features.

    Features:
    - Number of sessions
    - Total session duration
    - Total download traffic
    - Total upload traffic
    - Total traffic
    """

    user_features = (
        df.groupby("MSISDN/Number")
        .agg(
            Number_of_Sessions=("MSISDN/Number", "size"),
            Total_Duration_ms=("Dur. (ms)", "sum"),
            Total_DL_Bytes=("Total DL (Bytes)", "sum"),
            Total_UL_Bytes=("Total UL (Bytes)", "sum")
        )
        .reset_index()
    )

    user_features["Total_Traffic_Bytes"] = (
        user_features["Total_DL_Bytes"] +
        user_features["Total_UL_Bytes"]
    )

    return user_features

def build_experience_features(df):
    """
    Create customer-level experience features.

    Features:
    - Average TCP downlink retransmission
    - Average TCP uplink retransmission
    - Average downlink RTT
    - Average uplink RTT
    - Average downlink throughput
    - Average uplink throughput
    """

    experience_features = (
        df.groupby("MSISDN/Number")
        .agg(
            Avg_TCP_DL_Retrans=("TCP DL Retrans. Vol (Bytes)", "mean"),
            Avg_TCP_UL_Retrans=("TCP UL Retrans. Vol (Bytes)", "mean"),
            Avg_RTT_DL=("Avg RTT DL (ms)", "mean"),
            Avg_RTT_UL=("Avg RTT UL (ms)", "mean"),
            Avg_Throughput_DL=("Avg Bearer TP DL (kbps)", "mean"),
            Avg_Throughput_UL=("Avg Bearer TP UL (kbps)", "mean")
        )
        .reset_index()
    )

    return experience_features

def build_feature_store(df):
    """
    Build the customer-level feature store by combining
    engagement and experience features.
    """

    engagement_features = build_engagement_features(df)
    experience_features = build_experience_features(df)

    feature_store = engagement_features.merge(
        experience_features,
        on="MSISDN/Number",
        how="inner"
    )

    return feature_store