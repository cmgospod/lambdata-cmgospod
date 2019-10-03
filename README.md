# lambdata-cmgospod
Test repo for Unit 3


This repo contains two functions for use on pandas DataFrames, as well as an experimental rewrite of one as a class and a test file to verify correctness.

The first function, conc, adds any number of lists as extra columns at the end of a pandas DataFrame. To use the function, pass the DataFrame, followed by a dictionary. This dictionary should have the names you want the new columns to have as keys, and the lists themselves as values. As always, the lists must have the same length as the DataFrame has rows.

The second function, timesplitter, splits a datetime function into month, day, and year columns, optionally deleting the original. To use the function, pass the DataFrame and the name of the column you would like the function to act on. Note that timesplitter will initially run pandas' to_datetime function on the column, so it is not necessary to convert the column to the datetime format beforehand as long as it is something to_datetime can handle. Check the documentation for that function for more detail. Additionally, you may pass a boolean to determine whether or not to remove the column after splitting it.

The Conc class is just a rewrite of the conc function as a class. It takes the same arguments, but you need to run the serializer function to perform the same functionality.