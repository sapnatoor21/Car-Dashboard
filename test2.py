import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Title
st.title("Car Dashboard")

# Columns
col1, col2, col3 = st.columns(3)

# Metrics
with col1:
    st.metric("Speed", "60 mph")
with col2:
    st.metric("Fuel Level", "75%", delta="-5%")
with col3:
    st.metric("Distance", "120 miles", delta="+10 miles")

# Chart
chart_data = pd.DataFrame({
    'Speed': np.random.randint(50, 70, 10),
    'RPM': np.random.randint(1000, 2000, 10),
    'Time': np.arange(0, 10, 1)
})

fig = px.line(chart_data, x='Time', y=['Speed', 'RPM'], title="Speed and RPM over Time")
st.plotly_chart(fig)

# Performance Indicators (simulated gauges)
with st.expander("Engine Performance"):
    col4, col5 = st.columns(2)
    with col4:
        st.write("Oil Pressure: 75%")
        st.progress(0.75)  # Simulating a gauge with progress bar
    with col5:
        st.write("Temperature: 90%")
        st.progress(0.9)  # Simulating a gauge with progress bar

# Map for Route
with st.expander("Route"):
    st.map(pd.DataFrame({
        'lat': [37.7749, 37.7859],
        'lon': [-122.4194, -122.4364],
    }))

# Control
with st.expander("Control"):
    st.button("Start Engine")
    st.button("Turn Off Engine")
