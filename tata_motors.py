pip install yfinance matplotlib
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol for Tata Motors on NSE
ticker = 'TATAMOTORS.NS'

# Download historical data for last 6 months
data = yf.download(ticker, period='6mo')

# Plot the closing price
plt.figure(figsize=(10,5))
plt.plot(data.index, data['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.title('Tata Motors Closing Prices (Last 6 Months)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
