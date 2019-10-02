import pandas as pd
from cmgospod import conc
def timesplitter(frame, colname, remove=False):
"""This function takes a datetime column and splits it into day, month,
and year. Pass an optional remove argument to also remove the original
column.
"""
    datecol = pd.to_datetime(frame[colname])
    months = datecol.dt.month.tolist()
    days = datecol.dt.day.tolist()
    years = datecol.dt.year.tolist()
    frame = conc.conc(frame, {'days': days, 'months': months, 'years': years})
    if remove:
      del frame[colname]
    return frame
