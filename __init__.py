"""
Some helper functions
"""

import pandas as pd
import numpy as np

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(10))

def concentate(lst, frame):
    ser = pd.Series(lst)
    return pd.concat([frame, ser],axis=1)

def timesplitter(column):
