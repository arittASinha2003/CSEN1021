# https://beautiful-soup-4.readthedocs.io/en/latest/
# pip install requests, bs4

import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.gitam.edu")
# print(r.url)
# print(r.status_code)
# print(r.content)
soup = BeautifulSoup(r.content, "html5lib")
print(soup.prettify())