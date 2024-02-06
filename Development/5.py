import requests
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Replace 'your_api_key' with your Alpha Vantage API key
api_key = 'Z2ECKRUSXEP3HUYN'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={api_key}'

# Fetch data from the API
r = requests.get(url)
data = r.json()

# Extract relevant information
symbol = data['Meta Data']['2. Symbol']
time_series_data = data['Time Series (Daily)']

# Filter data for the last 3 months
today = datetime.now().date()
three_months_ago = today - timedelta(days=90)  # Assuming 30 days per month

# Create lists to store filtered data for plotting
dates = []
opens = []
highs = []
lows = []
closes = []

for date, values in time_series_data.items():
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    if three_months_ago <= date_obj <= today:
        if '4. close' in values:  # Skip missing data
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
fig.update_layout(title=f'Candlestick Chart for {symbol} (Last 3 Months)',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)

# Streamlit app
st.title(f'Candlestick Chart for {symbol} (Last 3 Months)')
st.plotly_chart(fig)
