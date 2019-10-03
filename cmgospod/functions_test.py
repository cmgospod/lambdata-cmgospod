
import unittest
from cmgospod.functions import conc, timesplitter

df = pd.DataFrame({'my_timestamp': pd.date_range('2016-1-1 15:00', periods=5)})
df['new_date'] = [d.date() for d in df['my_timestamp']]
df['new_time'] = [d.time() for d in df['my_timestamp']]
df['new_date'] = pd.to_datetime(df['new_date'])

df1 = df
df1['months'] = df['new_date'].dt.month
df1['days'] = df['new_date'].dt.day
df1['years'] = df['new_date'].dt.year



class TimeTests(unittest.TestCase):
    """Test the timesplitter function"""
    def test_time(self):
        self.assertEqual(timesplitter(df, 'new_date'), df1)

if __name__ == '__main__':
    unittest.main()
