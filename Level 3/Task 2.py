import sys
import subprocess
import streamlit as st
import pandas as pd
import plotly.express as px

# Automatically launch with streamlit runner if executed directly via standard python
if not st.runtime.exists():
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", __file__] + sys.argv[1:])
    except KeyboardInterrupt:
        pass
    sys.exit(0)

# Page configuration
st.set_page_config(
    page_title="Data Visualization Tool",
    page_icon="📊",
    layout="wide"
)

# Main Title
st.title("📊 Data Visualization Tool")
st.write("Upload a CSV file to explore data and create interactive visualizations.")

# Sidebar Controls
st.sidebar.header("📁 Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    # Read CSV safely
    try:
        data = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Unable to read the CSV file: {e}")
        st.stop()

    # Check for empty dataset
    if data.empty:
        st.warning("The uploaded CSV file is empty.")
        st.stop()

    # Get columns
    columns = data.columns.tolist()
    if not columns:
        st.error("The uploaded CSV file does not contain any valid columns.")
        st.stop()

    # Dataset Information Section
    st.subheader("📋 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", data.shape[0])
    col2.metric("Total Columns", data.shape[1])
    col3.metric("Missing Values", int(data.isnull().sum().sum()))

    with st.expander("🔍 Preview Dataset"):
        st.dataframe(data, use_container_width=True)

    # Visualization Controls in Sidebar
    st.sidebar.subheader("📈 Visualization Settings")
    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"]
    )

    x_column = st.sidebar.selectbox("Select X-axis Column", columns)

    y_column = None
    if chart_type != "Histogram":
        y_column = st.sidebar.selectbox("Select Y-axis Column", columns)

    color_options = ["None"] + columns
    color_column = st.sidebar.selectbox("Group by Color (Optional)", color_options)
    color_arg = None if color_column == "None" else color_column

    # Main Chart Display
    st.subheader("📊 Interactive Visualization")

    if chart_type == "Histogram":
        fig = px.histogram(
            data,
            x=x_column,
            color=color_arg,
            title=f"Histogram of {x_column}"
        )

    elif chart_type == "Bar Chart":
        fig = px.bar(
            data,
            x=x_column,
            y=y_column,
            color=color_arg,
            title=f"Bar Chart: {y_column} vs {x_column}"
        )

    elif chart_type == "Line Chart":
        if not pd.api.types.is_numeric_dtype(data[y_column]):
            st.warning(f"Note: Column '{y_column}' is non-numeric. Line charts work best with numerical data.")

        fig = px.line(
            data,
            x=x_column,
            y=y_column,
            color=color_arg,
            title=f"Line Chart: {y_column} vs {x_column}"
        )

    elif chart_type == "Scatter Plot":
        if not pd.api.types.is_numeric_dtype(data[y_column]):
            st.warning(f"Note: Column '{y_column}' is non-numeric. Scatter plots work best with numerical data.")

        fig = px.scatter(
            data,
            x=x_column,
            y=y_column,
            color=color_arg,
            title=f"Scatter Plot: {y_column} vs {x_column}"
        )

    # Render Plotly chart reactively
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👈 Please upload a CSV file using the sidebar panel to begin.")