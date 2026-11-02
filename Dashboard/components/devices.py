import pandas as pd
import streamlit as st

def show_devices(engine):

    df = pd.read_sql(
        """
        SELECT *
        FROM Devices
        """,
        engine
    )

    st.subheader("Devices")

    st.dataframe(
        df,
        use_container_width=True
    )