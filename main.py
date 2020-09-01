import os
import numpy as np
import pandas as pd


def compute_max_profit(list_exchange_rates):
    mins = np.minimum.accumulate(list_exchange_rates)
    return max(list_exchange_rates - mins)  
    # of course this is just an example, you need to add some codes here


if __name__ == "__main__":
    # load your data frame from data/exchange_rate.aud.06_2020.07_2020.csv
    df = pd.read_csv('data/exchange_rate.aud.06_2020.07_2020.csv')
    # convert to list
    list_exchange_rates = []
    list_exchange_rates = df['rate'].values[5:-15].tolist()
    # compute max profit we can achieve
    max_profit = compute_max_profit(list_exchange_rates)

    print('After many complicate calculations ...')
    print('Max profit we can get is', max_profit)
