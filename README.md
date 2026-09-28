# Tick Data OHLC Resampler

A Python script that converts raw tick-level trade data (individual price/volume events with timestamps) into standard OHLC (Open-High-Low-Close) bars, a common step in financial data processing.

## How it works
- Takes a series of timestamped trade prices and volumes
- Sets the timestamps as the DataFrame index
- Resamples the price data into 1-minute bars, calculating Open, High, Low, and Close for each interval
- Sums the volume within each 1-minute interval

## How to run
```bash
python ohlc_resampler.py
```

## What I learned
- Using `pd.to_datetime()` to convert timestamp strings into a proper datetime format
- Setting a datetime column as a DataFrame index to enable time-based operations
- Using `.resample('1min')` to group irregular time-series data into fixed intervals
- Using `.ohlc()` to calculate Open/High/Low/Close in one step, instead of computing each manually
- Aggregating volume separately with `.resample().sum()` alongside the price resampling

## Dependencies
Requires pandas:
```bash
pip install pandas
```
