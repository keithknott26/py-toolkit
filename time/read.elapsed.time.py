# Creating time stamps with the datetime module
# For more information, see http://effbot.org/librarybook/datetime.htm

from datetime import datetime as dt
ts = dt.now()
# This creates a timestamp object containing date and time elements that can be retrieved individually, with examples as shown below:
y = ts.year # 2017
mo = ts.month # 10
d = ts.day # 24
h = ts.hour # 18
mi = ts.minute # 8
s = ts.second # 39
f = ts.microsecond # 141000

# Convert numeric output to string; pad with zero to get two digits
mi = (str(ts.minute)).zfill(2)
# This yields '08'

# Get the elapsed time between ts1 and ts2, which are timestamp objects created at different times
delta = ts2 - ts1
# This creates a time difference object from which you can retrieve days, seconds, and microseconds, with examples shown below:
days = delta.days # 0
seconds = delta.seconds # 1279
micro = delta.microseconds # 508000

# Extract minutes and seconds as follows:
minutes = delta.seconds/60 # 21
seconds = delta.seconds%60 # 19


# Here's a handy function:
def GetElapsedTime (t1, t2):
   """Gets the time elapsed between the start time (t1) and the finish time (t2)."""
   delta = t2 - t1
   (d, m, s) = (delta.days, delta.seconds/60, delta.seconds%60)
   (h, m) = (m/60, m%60)
   deltaString = '%s days, %s hours, %s minutes, %s seconds' % (str(d), str(h), str(m), str(s))
   return deltaString