# V1 - working code that is not written well

# these are the external libraries we will be using, we need to import them
# NOTE: before importing, we had to install them!  this is done with pip, from the terminal.  ex. 'sudo pip install bs4'
import bs4
import requests

# get cnn main health page using the requests library
# this is fetching the raw html
res = requests.get('https://www.cnn.com/health')
res.raise_for_status()

# get all links with in the html using the beautifulsoup library
# beautifulsoup parses html and makes searching for features easy
exampleSoup = bs4.BeautifulSoup(res.text, features="html.parser")
link_elements = exampleSoup.find_all('a', href=True)

# loop through all the links, add to our link_array 
# some links already have a prefix, some dont.  
link_array = []
for link_element in link_elements:
  if ('www' in link_element['href']) or ('http' in link_element['href']):
    link_array.append(link_element['href'])
  else:
    link_array.append('https://www.cnn.com' + link_element['href'])

# printing all of our links in our link_array
print('Printing link array:')
for link in link_array:
  print(link)
