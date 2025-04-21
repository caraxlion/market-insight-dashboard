# Use plotly to create interactive charts

import plotly.graph_objs as go

def plot_price(data, sma=None):
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Close Price'))
  if sma is not None:
    fig.add_trace(go.Scatter(x=data.index, y=sma, name='SMA'))
  return fig
