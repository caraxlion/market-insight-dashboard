# Add functions for moving averages, RSI, etc.

def calculate_sma(df,window)
  return df['Close']rolling(window=window).mean()
