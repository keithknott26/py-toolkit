## Import all Gists from a Github users account

import subprocess
import sys
import pandas as pd
import json 

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

# Used for both public and private
username = input("Username:") 
# Use password if you want both private and public gists, otherwise use "".
password = input("Password (blank for public only):") 

proc = subprocess.Popen(["curl", "--user", username + ":" + 
                        password, "https://api.github.com/users/" + username + "/gists"], 
                        stdout = subprocess.PIPE)
      
output = StringIO(proc.communicate()[0].decode('utf-8'))
# print(output.getvalue())

# Convert json to dataframe
data = pd.DataFrame(json.loads(output.getvalue()))
data

## Filter gists by terms
import numpy as np
text = input("Search terms:").lower()
searchfor = text.split()
filteredData = data[data.description.str.lower()
   .str.contains('|'.join(searchfor))[['description','files','url']]
for i in filteredData.description:
    print(i)
filteredData

## Input index of filtered gists from table above
indexNum = int(input("Choose index # from Above:"))
filteredFiles = list(filteredData[filteredData.index ==   indexNum].files)[0]
keys = list(filteredFiles.keys())
## Print each sub gist
for key in keys:
    print(filteredFiles[key]['raw_url'])

## Executing code directly fromm Gists
# Confirm Jupyter Notebook uses Conda env Python version
    # Install: pip install fix_yahoo_finance --upgrade --no-cache-dir
    # Install: pip install git+https://github.com/pydata/pandas-datareader.git
##import requests
#url = "https://gist.githubusercontent.com/ZeccaLehn/9d4946bf1fe07c27c3ad10ef83093413/raw/f2d6f8c1c183a8c676cb2f797f3482c7989fce0e/multipleStocks.py"
#response = requests.get(url)
#exec(response.text)
#allData
## Note: For JSON Direct downloads
    ## proc = subprocess.Popen(["curl", url], stdout = subprocess.PIPE)
    ## output = StringIO(proc.communicate()[0].decode('utf-8'))
    ## output.getvalue()
    ## output = json.loads(output.getvalue())
    ## output