import datetime

# Given a list of datetime objects, subtract an element from the next in the list and if the difference is > 10m add
# the timestamp to a dropout time dictionary along with the time difference.


def dropout_detector(data_input: list):
    dropout_times = {}
    time_eleven_mins = datetime.timedelta(minutes=11)

    for timestamp in data_input:
        if data_input.index(timestamp) < (len(data_input) - 1):
            time_difference = data_input[data_input.index(timestamp) + 1] - timestamp

            if time_difference > time_eleven_mins:
                dropout_times[time_difference] = timestamp

    return dropout_times
