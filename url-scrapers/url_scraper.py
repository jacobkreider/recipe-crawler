''' Uses Beautiful Soup to scrape all top recipes URLs from our chosen sites'''

import top_recipes_urls
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.allrecipes.com/recipes/16492/everyday-cooking/special-collections/allrecipes-allstars/") # Insert your URL to extract
bsObj = BeautifulSoup(html.read())

allrecipe_urls = []

for link in bsObj.find_all('a'):
    allrecipe_urls.append(link.get('href'))

print(allrecipe_urls)