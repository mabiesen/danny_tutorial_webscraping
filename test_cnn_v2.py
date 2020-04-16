# V2 - Using functions

import bs4
import requests

# get cnn main health page
# this is fetching the raw html
def get_cnn_health_html():
  result = requests.get('https://www.cnn.com/health')
  result.raise_for_status()
  return result.text #we dont need the result status detail, just html

# get all links with in the page using beautifulsoup
# beautifulsoup parses html and makes searching for features easy
def get_links_from_html(html):
  exampleSoup = bs4.BeautifulSoup(html, features="html.parser")
  link_elements = exampleSoup.find_all('a', href=True)
  full_urls = []
  for link_element in link_elements:
    if ('www' in link_element['href']) or ('http' in link_element['href']):
      link_array.append(link_element['href'])
    else:
      link_array.append('https://www.cnn.com' + link_element['href'])
  return full_urls

# call the functions that we created
html = get_cnn_health_html()
links = get_links_from_html(html)

#print the links
for link in links:
  print(link)
