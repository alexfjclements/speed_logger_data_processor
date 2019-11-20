import pandas as pd
import matplotlib.dates as mpl_d
from src.bytes_formatter import datetime_conversion, format_bytes
from src.custom_comparison import dropout_detector

data = pd.read_csv("log.csv")

data.columns = ["Date/Time", "IP Address", "Latency (m/s)", "Download Speed", "Upload Speed", "Provider"]

download_speed_list = data["Download Speed"]
upload_speed_list = data["Upload Speed"]
timestamps = datetime_conversion(data["Date/Time"])
latencies = data["Latency (m/s)"]

# Upload, download max, min, and average. Basic details
print(f"Sample size: {len(download_speed_list)} entries. \n")

print(f"Max upload speed: {format_bytes(upload_speed_list.max())}")
print(f"Min upload speed: {format_bytes(upload_speed_list.min())}")
print(f"Average upload speed: {format_bytes(sum(upload_speed_list)/len(upload_speed_list))} \n")

print(f"Max download speed: {format_bytes(download_speed_list.max())}")
print(f"Min download speed: {format_bytes(download_speed_list.min())}")
print(f"Average download speed: {format_bytes(sum(download_speed_list)/len(download_speed_list))} \n")

print(f"Max latency: {latencies.max()} \n")

print(f"Dropout times: {dropout_detector(timestamps)}")

mpl_timestamps = mpl_d.date2num(timestamps)
# plt.plot(timestamps, upload_speed_list)
# plt.show()
