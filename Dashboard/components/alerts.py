import pandas as pd
import streamlit as st

def show_alerts(engine):

    try:
        df = pd.read_sql(
            """
            SELECT *
            FROM Alerts
            ORDER BY CreatedAt DESC
            """,
            engine
        )

        st.subheader("Alerts")

        st.dataframe(
            df,
            use_container_width=True
        )

    except:
        st.info(
            "Alerts table not available yet."
        )