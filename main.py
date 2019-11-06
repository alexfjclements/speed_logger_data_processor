import pandas as pd
import matplotlib as mpl

data = pd.read_csv("log.csv")

data.columns = ["Date/Time", "IP Address", "Latency", "Download", "Upload", "Provider"]

print(data)
