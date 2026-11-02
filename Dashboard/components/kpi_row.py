import pandas as pd
import streamlit as st

def show_kpis(engine):

    total_devices = pd.read_sql(
        "SELECT COUNT(*) AS TotalDevices FROM Devices",
        engine
    ).iloc[0]["TotalDevices"]

    total_readings = pd.read_sql(
        "SELECT COUNT(*) AS TotalReadings FROM DeviceReadings",
        engine
    ).iloc[0]["TotalReadings"]

    latest_reading = pd.read_sql(
        """
        SELECT MAX([Timestamp]) AS LatestReading
        FROM DeviceReadings
        """,
        engine
    ).iloc[0]["LatestReading"]

    try:
        total_alerts = pd.read_sql(
            "SELECT COUNT(*) AS TotalAlerts FROM Alerts",
            engine
        ).iloc[0]["TotalAlerts"]
    except:
        total_alerts = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Devices", total_devices)
    col2.metric("Total Readings", total_readings)
    col3.metric("Total Alerts", total_alerts)
    formatted_time = latest_reading.strftime("%d-%b-%Y")
    col4.metric("Latest Reading",formatted_time)
