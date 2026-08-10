import os
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Tesla Stock Price Prediction",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .info-box {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📈 Tesla Stock Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">LSTM-Based Stock Price Forecasting</div>',
    unsafe_allow_html=True
)

st.write(
    """
    This project uses a Long Short-Term Memory (LSTM) neural network
    to analyze historical Tesla (TSLA) stock prices and predict stock
    price trends.
    """
)

st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📌 Project Information")

st.sidebar.write("**Company:** Tesla (TSLA)")
st.sidebar.write("**Model:** LSTM")
st.sidebar.write("**Framework:** TensorFlow / Keras")
st.sidebar.write("**Data Source:** Yahoo Finance")
st.sidebar.write("**Language:** Python")

st.sidebar.divider()

st.sidebar.info(
    """
    This application is created for educational
    and machine learning demonstration purposes.
    """
)

# --------------------------------------------------
# About the Project
# --------------------------------------------------

st.header("🤖 About the Project")

st.write(
    """
    Tesla Stock Price Prediction is a machine learning project that
    uses an LSTM neural network to learn patterns from historical
    Tesla stock prices.

    LSTM networks are particularly useful for time-series problems
    because they can learn relationships between previous and
    future observations.
    """
)

# --------------------------------------------------
# Technologies
# --------------------------------------------------

st.header("🛠️ Technologies Used")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Language", "Python")

with col2:
    st.metric("Model", "LSTM")

with col3:
    st.metric("Framework", "TensorFlow")

with col4:
    st.metric("Data", "Yahoo Finance")

st.divider()

# --------------------------------------------------
# Prediction Graph
# --------------------------------------------------

st.header("📊 Prediction Results")

image_path = "tesla_prediction.png"

if os.path.exists(image_path):

    st.image(
        image_path,
        caption="Actual vs Predicted Tesla Stock Prices",
        width="stretch"
    )

    st.success(
        "✅ Prediction graph loaded successfully."
    )

else:

    st.error(
        "❌ tesla_prediction.png was not found in the project folder."
    )

# --------------------------------------------------
# Model Information
# --------------------------------------------------

st.header("🧠 Trained LSTM Model")

model_path = "tesla_lstm_model.keras"

if os.path.exists(model_path):

    st.success(
        "✅ Trained LSTM model is available."
    )

    st.write(
        """
        The trained model is stored in the repository as:
        """
    )

    st.code("tesla_lstm_model.keras")

else:

    st.warning(
        "⚠️ Trained model file was not found."
    )

# --------------------------------------------------
# Project Workflow
# --------------------------------------------------

st.header("🔄 Project Workflow")

steps = [
    "Collect historical Tesla stock data using yFinance.",
    "Clean and preprocess the stock price data.",
    "Normalize the data for neural network training.",
    "Create training and testing sequences.",
    "Build the LSTM neural network.",
    "Train the model using historical stock data.",
    "Generate predictions using the trained model.",
    "Compare actual and predicted stock prices."
]

for number, step in enumerate(steps, 1):
    st.write(f"**{number}.** {step}")

# --------------------------------------------------
# Project Files
# --------------------------------------------------

st.header("📁 Project Files")

files = [
    "app.py",
    "train_model.py",
    "requirements.txt",
    "tesla_lstm_model.keras",
    "tesla_prediction.png",
    "README.md"
]

for file in files:

    if os.path.exists(file):
        st.write(f"✅ `{file}`")
    else:
        st.write(f"⚪ `{file}`")

# --------------------------------------------------
# Disclaimer
# --------------------------------------------------

st.divider()

st.warning(
    """
    ⚠️ Disclaimer: This project is developed for educational and
    demonstration purposes only. Stock market predictions are
    inherently uncertain and this application should not be
    considered financial advice.
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Developed by <b>Chaitanya Penmetsa</b><br>
        Tesla Stock Price Prediction using LSTM
    </div>
    """,
    unsafe_allow_html=True
)