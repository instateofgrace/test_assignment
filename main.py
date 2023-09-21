import dask.dataframe as dd
import pandas as pd
import plotly.graph_objects as go


def read_trades(file_path):
    """
    Read trades from the provided CSV file using Dask.
    """
    trades = dd.read_csv(file_path, parse_dates=['TS'])
    return trades


def form_candlesticks(trades, interval):
    """
    Form candlesticks based on the provided time interval.
    """
    if isinstance(trades, dd.DataFrame):  # Check if trades is a Dask DataFrame
        trades = trades.compute()  # Call compute() only if trades is a Dask DataFrame
    trades.set_index('TS', inplace=True)
    interval = interval.replace('m', 'T')  # Convert 'm' to 'T' for resampling
    ohlc = trades['PRICE'].resample(interval).ohlc()
    return ohlc.dropna()


def calculate_ema(prices, length):
    """
    Calculate the Exponential Moving Average (EMA) for the given length.
    """
    ema = prices.ewm(span=length, adjust=False).mean()
    return ema


def plot_candlesticks(candlesticks, ema):
    """
    Plot candlesticks and EMA using Plotly.
    """
    fig = go.Figure(data=[go.Candlestick(x=candlesticks.index,
                                         open=candlesticks['open'],
                                         high=candlesticks['high'],
                                         low=candlesticks['low'],
                                         close=candlesticks['close'],
                                         name='Candlesticks'),
                          go.Scatter(x=candlesticks.index, y=ema, name=f'EMA {length} periods',
                                     line=dict(color='red'))])
    fig.show()


def get_user_input():
    """
    Get user input for the timeframe and EMA period with validation.
    """
    while True:
        interval = input(
            "Enter the timeframe (e.g., 5m for 5 minutes, 1H for 1 hour): ").strip()  # Changed prompt to '5m'
        if interval[-1] in ['m', 'H', 'D'] and interval[:-1].isdigit():  # Changed 'T' to 'm'
            break
        else:
            print("Invalid timeframe. Please use 'm' for minutes, 'H' for hours, 'D' for days and a number before it.")

    while True:
        try:
            length = int(input("Enter the EMA period (e.g., 14): ").strip())
            if length > 0:
                break
            else:
                print("EMA period should be a positive integer.")
        except ValueError:
            print("Invalid input. EMA period should be an integer.")

    return interval, length


if __name__ == "__main__":
    file_path = "prices.csv"
    interval, length = get_user_input()  # Get validated user input for timeframe and EMA period
    trades = read_trades(file_path)
    candlesticks = form_candlesticks(trades, interval)
    ema = calculate_ema(candlesticks['close'], length)
    plot_candlesticks(candlesticks, ema)
