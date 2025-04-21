import yfinance as yf

def get_data(ticker, start, end):
  retrun yf.download(ticker, start=start, end-end)
