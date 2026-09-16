import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page title
st.title("Data Visualization Tool")

st.write("Upload a CSV file to create interactive visualizations.")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:

    # Read CSV file
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.dataframe(data)

    # Show dataset information
    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])

    # Select columns
    columns = data.columns.tolist()

    x_column = st.selectbox("Select X-axis column", columns)

    y_column = st.selectbox("Select Y-axis column", columns)

    # Select chart type
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"]
    )

    if st.button("Generate Chart"):

        st.subheader("Visualization")

        if chart_type == "Bar Chart":
            fig = px.bar(
                data,
                x=x_column,
                y=y_column,
                title="Bar Chart"
            )
            st.plotly_chart(fig)

        elif chart_type == "Line Chart":
            fig = px.line(
                data,
                x=x_column,
                y=y_column,
                title="Line Chart"
            )
            st.plotly_chart(fig)

        elif chart_type == "Scatter Plot":
            fig = px.scatter(
                data,
                x=x_column,
                y=y_column,
                title="Scatter Plot"
            )
            st.plotly_chart(fig)

        elif chart_type == "Histogram":
            fig = px.histogram(
                data,
                x=x_column,
                title="Histogram"
            )
            st.plotly_chart(fig)
            