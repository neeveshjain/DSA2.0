import requests
import plotly.graph_objects as go

# Replace 'your_api_key' with your Alpha Vantage API key
api_key = 'your_api_key'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={api_key}'

# Fetch data from the API
r = requests.get(url)
data = r.json()

# Extract relevant information
symbol = data['Meta Data']['2. Symbol']
time_series_data = data['Time Series (Daily)']

# Create lists to store data for plotting
dates = []
opens = []
highs = []
lows = []
closes = []

for date, values in time_series_data.items():
    dates.append(date)
    opens.append(float(values['1. open']))
    highs.append(float(values['2. high']))
    lows.append(float(values['3. low']))
    closes.append(float(values['4. close']))

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opens,
                                     high=highs,
                                     low=lows,
                                     close=closes)])

# Customize the layout
fig.update_layout(title=f'Candlestick Chart for {symbol}',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)

# Show the plot
fig.show()
