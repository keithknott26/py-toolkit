#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

# website to scrap (movie database)
URL_ROOT = "https://www.themoviedb.org/"

# Find movie URL
endpoint = URL_ROOT + "discover/movie"

# payload, to provide parameters for the url
payload = {'sort_by': 'popularity.desc', 'primary_release_year': '1945'}
# You can dinamically build your query adding params to the payload
year = input('Search most popoular movie in (year): ')
payload['primary_release_year'] = year

# use request to get the response from the API
try:
    response = requests.get(endpoint, payload)
    # check that we got a page back
    if response.status_code is not requests.codes.ok:
        print('Error with this url {}'.format(response.url))
    else:
        # use BeautifulSoup to parse the HTML file returned
        soup = BeautifulSoup(response.text, "html.parser")
        # get all the tag title results
        # i.e <a alt="Desire" class="title result" href="/movie/86331" id="movie_86331" title="Desire">Desire</a>
        tags = soup.find_all('a', class_='title result')
        # get the title (form the tag value)
        titles = [tag.string for tag in tags]
        # print order by popularity
        print("YEAR: {}".format(year))
        for i, t in enumerate(titles, start=1):
            print("#{} {}".format(i, t))
except Exception as ex:
    print('Ops, something went wrong!')
    print(ex)
