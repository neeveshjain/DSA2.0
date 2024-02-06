import yfinance as yf
import pandas as pd
import streamlit as st
import datetime

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def main():
    st.title("Stock Price Visualization")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
    start_date = st.sidebar.date_input("Start Date", datetime.date(2021, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime.date(2022, 1, 1))

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Display raw data
    st.subheader(f"Raw Stock Price Data for {ticker}")
    st.write(stock_data)

    # Plot closing prices
    st.subheader(f"Closing Prices for {ticker}")
    st.line_chart(stock_data['Close'])

if __name__ == "__main__":
    main()
