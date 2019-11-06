import pandas as pd
import matplotlib.dates as mpl_d
import matplotlib.pyplot as plt
from datetime import datetime
from bytes_formatter import format_speed, datetime_conversion

data = pd.read_csv("log.csv")

data.columns = ["Date/Time", "IP Address", "Latency (m/s)", "Download Speed", "Upload Speed", "Provider"]

download_speed_list = data["Download Speed"]
upload_speed_list = data["Upload Speed"]
timestamps = datetime_conversion(data["Date/Time"])

download_speeds, download_labels, upload_speeds, upload_labels = format_speed(download_speed_list, upload_speed_list)

# Basic label comparison
if download_labels.count(download_labels[0]) == len(download_labels):
    single_download_label = download_labels[0]

if upload_labels.count(upload_labels[0]) == len(upload_labels):
    single_upload_label = upload_labels[0]

# Interesting, but requires solution to unit conversion issue to be properly meaningful
mpl_timestamps = mpl_d.date2num(timestamps)
plt.plot(timestamps, upload_speeds)
plt.show()
