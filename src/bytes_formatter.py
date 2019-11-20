"""
Python format_bytes function, source:
https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
"""

from datetime import datetime


def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'


# no longer required?
def format_speed(download, upload):
    download_speeds = []
    download_labels = []
    upload_speeds = []
    upload_labels = []

    for entry in download:
        speed, label = format_bytes(entry)
        download_speeds.append(speed)
        download_labels.append(label)

    for entry in upload:
        speed, label = format_bytes(entry)
        upload_speeds.append(speed)
        upload_labels.append(label)

    # returning lists of labels, though not yet doing anything to process or compare them.
    # TODO compare labels
    return download_speeds, download_labels, upload_speeds, upload_labels


def datetime_conversion(datetime_list):
    converted_datetime = []

    for timestamp in datetime_list:
        converted_datetime.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))

    return converted_datetime
