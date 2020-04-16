# this version works, but is spaghetti

import bs4
import requests

# get cnn main health page
# this is fetching the raw html
res = requests.get('https://www.cnn.com/health')
res.raise_for_status()

# get all links with in the page using beautifulsoup
# beautifulsoup parses html and makes searching for features easy
exampleSoup = bs4.BeautifulSoup(res.text, features="html.parser")
link_elements = exampleSoup.find_all('a', href=True)

# loop all links
link_array = []
for link_element in link_elements:
  if ('www' in link_element['href']) or ('http' in link_element['href']):
    link_array.append(link_element['href'])
  else:
    link_array.append('https://www.cnn.com' + link_element['href'])

# printing all of our links
print('Printing link array:')
for link in link_array:
  print(link)
