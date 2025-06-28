import streamlit as st
import pandas as pd

st.set_page_config(page_title="Intrusion Detection Dashboard", layout="wide")

st.title("📊 Intrusion Detection System Dashboard")
st.markdown("Real-time view of logged suspicious network activity.")

try:
    df = pd.read_csv("logs.csv")
    st.dataframe(df, use_container_width=True)

    # Filter view
    unique_ips = df["Source IP"].unique()
    selected_ip = st.selectbox("Filter by Source IP:", ["All"] + list(unique_ips))

    if selected_ip != "All":
        df = df[df["Source IP"] == selected_ip]

    st.write(f"🚨 Total Alerts: {len(df)}")
    st.dataframe(df.tail(10), use_container_width=True)

except FileNotFoundError:
    st.warning("No logs available yet. Start the IDS system to begin detection.")
