import pandas as pd
import plotly.express as px
import streamlit as st

def show_humidity(engine):

    df = pd.read_sql(
        """
        SELECT
            Timestamp,
            DeviceId,
            Humidity
        FROM DeviceReadings
        ORDER BY Timestamp
        """,
        engine
    )

    fig = px.line(
        df,
        x="Timestamp",
        y="Humidity",
        color="DeviceId",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )