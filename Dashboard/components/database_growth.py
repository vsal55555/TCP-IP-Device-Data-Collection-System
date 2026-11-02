import pandas as pd
import plotly.express as px
import streamlit as st

def show_growth(engine):

    df = pd.read_sql(
        """
        SELECT
            CAST(Timestamp AS DATE) AS ReadingDate,
            COUNT(*) AS TotalReadings
        FROM DeviceReadings
        GROUP BY CAST(Timestamp AS DATE)
        ORDER BY ReadingDate
        """,
        engine
    )

    fig = px.bar(
        df,
        x="ReadingDate",
        y="TotalReadings",
        title="Database Growth"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )