import streamlit as st
import pandas as pd
import numpy as np

st.title("MLOps Lab Dashboard")
st.write("Created by Sanjana Menon")

# Sample metrics
col1, col2, col3 = st.columns(3)
col1.metric("Model Accuracy", "94.5%", "+2.1%")
col2.metric("Tests Passed", "12/12", "100%")
col3.metric("Build Status", "✅ Pass")

# Sample data visualization
st.subheader("Model Performance Over Time")
chart_data = pd.DataFrame(
    np.random.randn(20, 3) * 0.1 + 0.9,
    columns=['Accuracy', 'Precision', 'Recall']
)
st.line_chart(chart_data)

st.subheader("CI/CD Pipeline Status")
st.success("All GitHub Actions workflows passing!")