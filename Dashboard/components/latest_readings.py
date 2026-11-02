import pandas as pd
import streamlit as st

def show_readings(engine):

    df = pd.read_sql(
        """
        SELECT TOP 50 *
        FROM DeviceReadings
        ORDER BY Timestamp DESC
        """,
        engine
    )

    st.subheader("Latest Readings")

    st.dataframe(
        df,
        use_container_width=True
    )