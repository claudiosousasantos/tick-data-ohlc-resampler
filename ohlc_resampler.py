import pandas as pd

timestamps = pd.to_datetime([
    "2024-01-01 09:30:01", "2024-01-01 09:30:15", "2024-01-01 09:30:40",
    "2024-01-01 09:30:55", "2024-01-01 09:31:05", "2024-01-01 09:31:20",
    "2024-01-01 09:31:50", "2024-01-01 09:32:10", "2024-01-01 09:32:30",
    "2024-01-01 09:32:58"
])
prices = [100.0, 100.5, 101.2, 100.8, 101.0, 101.5, 101.3, 102.0, 101.8, 102.5]
volumes = [200, 150, 300, 100, 250, 400, 180, 220, 190, 310]

df = pd.DataFrame({"price": prices, "volume": volumes}, index=timestamps)

ohlc = df['price'].resample('1min').ohlc()
ohlc['volume'] = df['volume'].resample('1min').sum()

print(ohlc)