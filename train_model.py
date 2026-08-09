import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


# 1. Download Tesla stock data
print("Downloading Tesla stock data...")

data = yf.download(
    "TSLA",
    start="2015-01-01",
    end="2026-01-01",
    auto_adjust=True
)

print("Data downloaded successfully!")
print(data.head())


# 2. Select closing price
close_data = data[["Close"]].values


# 3. Scale the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_data)


# 4. Create training sequences
sequence_length = 60

X = []
y = []

for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i - sequence_length:i, 0])
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)


# 5. Reshape data for LSTM
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

print("Input shape:", X.shape)
print("Output shape:", y.shape)


# 6. Build LSTM model
model = Sequential()

model.add(
    LSTM(
        units=50,
        return_sequences=True,
        input_shape=(X.shape[1], 1)
    )
)

model.add(Dropout(0.2))

model.add(
    LSTM(
        units=50,
        return_sequences=False
    )
)

model.add(Dropout(0.2))

model.add(Dense(units=25))
model.add(Dense(units=1))


# 7. Compile model
model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)


# 8. Train model
print("Training the LSTM model...")

model.fit(
    X,
    y,
    epochs=10,
    batch_size=32,
    verbose=1
)


# 9. Save the trained model
model.save("tesla_lstm_model.keras")

print("Model saved successfully!")


# 10. Generate predictions
predicted_prices = model.predict(X)

predicted_prices = scaler.inverse_transform(predicted_prices)


# 11. Plot actual vs predicted prices
plt.figure(figsize=(12, 6))

plt.plot(
    close_data,
    label="Actual Tesla Price"
)

plt.plot(
    range(sequence_length, len(predicted_prices) + sequence_length),
    predicted_prices,
    label="Predicted Tesla Price"
)

plt.title("Tesla Stock Price Prediction using LSTM")
plt.xlabel("Time")
plt.ylabel("Stock Price (USD)")

plt.legend()
plt.grid(True)

plt.savefig("tesla_prediction.png")

plt.show()

print("Prediction graph saved as tesla_prediction.png")