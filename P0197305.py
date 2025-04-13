import numpy as np


# Problem link: https://quera.org/problemset/197305

def moving_average(data_list, window_size):
    ma = []

    for i in range(0, len(data_list) - window_size + 1):
        ma.append(np.mean(data_list[i:i + window_size]))

    return np.round(np.array(ma), 2)