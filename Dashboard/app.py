import streamlit as st
from streamlit_autorefresh import st_autorefresh

from db import engine

from components.kpi_row import show_kpis
from components.devices import show_devices
from components.latest_readings import show_readings
from components.temperature_trend import show_temperature
from components.humidity_trend import show_humidity
from components.database_growth import show_growth
from components.alerts import show_alerts

st.set_page_config(
    page_title="TCP/IP Device Monitoring",
    layout="wide"
)

# Auto refresh every 5 seconds
st_autorefresh(
    interval=5000,
    key="refresh"
)

st.title(
    "TCP/IP Device Monitoring Dashboard"
)

show_kpis(engine)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Devices",
        "Alerts",
        "Readings",
        "Temperature",
        "Humidity",
        "Database Growth"
    ]
)

with tab1:
    show_devices(engine)

with tab2:
    show_alerts(engine)

with tab3:
    show_readings(engine)

with tab4:
    show_temperature(engine)

with tab5:
    show_humidity(engine)

with tab6:
    show_growth(engine)
    

