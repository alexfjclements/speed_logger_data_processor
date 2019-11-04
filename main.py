import pandas as pd
import matplotlib as mpl

data = pd.read_csv("log.csv")

# TODO get column header list from data file
headed_data = pd.DataFrame([data], columns=["Sequence", "Start", "End", "Coverage"])
