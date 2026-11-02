import pandas as pd
import plotly.express as px
import streamlit as st

def show_temperature(engine):

    df = pd.read_sql(
        """
        SELECT
            Timestamp,
            DeviceId,
            Temperature
        FROM DeviceReadings
        ORDER BY Timestamp
        """,
        engine
    )

    fig = px.line(
        df,
        x="Timestamp",
        y="Temperature",
        color="DeviceId",
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )