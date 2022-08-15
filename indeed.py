import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = 'https://www.indeed.com/companies/browse-companies'
html = requests.get(base_url)
print(html.status_code)