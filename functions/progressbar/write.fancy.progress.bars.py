#requires pip3 install alive-progress
#https://github.com/rsalmei/alive-progress

from alive_progress import alive_bar
import time

for x in 1000, 1500, 700, 0:
   with alive_bar(x) as bar:
       for i in range(1000):
           time.sleep(.005)
           bar()