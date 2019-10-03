import pandas as pd
def conc(frame, dictoflists):
    """This functions turns lists into new columns for a DataFrame.
    Takes the frame, followed by a dictionary with column names
    as keys and lists as values.
    """
    for key in dictoflists:
        ser = pd.Series(dictoflists[key], name=key)
        frame = pd.concat([frame, ser], axis=1)
    return frame

def timesplitter(frame, colname, remove=False):
    """This function takes a datetime column and splits it into
    day, month, and year. Pass an optional remove argument to
    also remove the original column.
    """
    from cmgospod.functions import conc
    datecol = pd.to_datetime(frame[colname])
    months = datecol.dt.month.tolist()
    days = datecol.dt.day.tolist()
    years = datecol.dt.year.tolist()
    frame = conc(frame, {'days': days, 'months': months, 'years': years})
    if remove:
      del frame[colname]
    return frame

class Conc():
    """Class for adding lists to DataFrames"""
    def __init__(self, frame, dictoflists):
      self.frame = frame
      self.dictoflists = dictoflists

    def serializer(self):
        """Performs the hard work of adding the lists to the DataFrame"""
      for key in self.dictoflists:
        ser = pd.Series(self.dictoflists[key], name=key)
        df2 = pd.concat([self.frame, ser], axis=1)
      return df2
