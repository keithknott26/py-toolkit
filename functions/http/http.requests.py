""" Snippets for making http requests """
import requests

""" The url to request """
URL = ''
""" Additional HTTP Headers (Use 'X-Requested-With' : 'XMLHttpRequest' to simulate AJAX """
HEADERS = {'X-Requested-With':'XMLHttpRequest'}

# Snippet for get requests.
""" The url parameters for the request"""
PARAMS = {'q' : 'Search'}
""" Contents of the request body. If a dictionary is passed it is converted to the post parameter format '<name>=<val>&<name2>=<val2>... """
REQUEST_BODY = 'asdfadfs'
# Make a get request.
r = requests.get(URL, params=PARAMS, headers=HEADERS, data=REQUEST_BODY)
# Available properties after the get request is executed.
print(r.url)
print(r.headers)
print(r.cookies)
print(r.status_code)
print(r.text)

# Snippet for post requests.
""" The form parameters for the request. If a dictionary is passed it is converted to the post parameter format '<name>=<val>&<name2>=<val2>... """
FORM_PARAMS = {'param1' : 'asdf', 'arrayparam' : ['a', 'b']} # If an array is passed as a value each the name is passed multiple times once with each value.
# Make a post request.
r = requests.post(URL, headers=HEADERS, data=FORM_PARAMS)
# Available properties after the get request is executed.
print(r.url)
print(r.headers)
print(r.cookies)
print(r.status_code)
print(r.text)
