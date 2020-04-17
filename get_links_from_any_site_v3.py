# V3 - accepts url argument from user, is not cnn specific

import bs4
import requests
from urllib.parse import urlparse

def get_url_from_user():
  url = input('Please supply a url: ')
  return url

def get_base_url_from_url(url):
  parsed_url = urlparse(url)
  base_url = parsed_url.netloc
  return base_url

# get cnn main health page
# this is fetching the raw html
def get_html_for_url(url):
  result = requests.get(url)
  result.raise_for_status()
  return result.text #we dont need the result status detail, just html

# get all links with in the page using beautifulsoup
# beautifulsoup parses html and makes searching for features easy
def get_links_from_html(html):
  exampleSoup = bs4.BeautifulSoup(html, features="html.parser")
  link_elements = exampleSoup.find_all('a', href=True)
  hrefs = []
  for link_element in link_elements:
    hrefs.append(link_element['href'])
  return hrefs

def get_full_urls_from_hrefs(href_array, base_url):
  return_array = []
  for href in href_array:
    if ('http' in href) or ('www' in href):
      return_array.append(href)
    else:
      return_array.append(base_url + href)
  return return_array

# call the functions that we created
url = get_url_from_user()
base_url = get_base_url_from_url(url)
html = get_html_for_url(url)
hrefs = get_links_from_html(html)
links = get_full_urls_from_hrefs(hrefs, base_url)

#print the links
for link in links:
  print(link)
