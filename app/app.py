# Build Streamlit UI and inlcude ticker input, date picker chart, 
# and import from other files

import streamlit as st
from app.data_loader import get_data
from app.analytics import calculate_sma
from app.visuals import plot_price

# The title of the dashboard
st.title("Market Insight Dashboard")

# market identifiers
ticker = st.text_input("Enter tock ticker (e.g. AAPL)", "AAPL")
start - st.date_input("Start date")
end = st.date_input("End date")

# loop
if ticker and start and end:
    data = get_data(ticker, start, end)
    sma = calculate_sma(data, window=20)
    fig = plot_price(data, sma)
    st.plotly_chart(fig)
