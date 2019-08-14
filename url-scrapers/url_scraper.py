''' Uses Beautiful Soup to scrape all top recipes URLs from our chosen sites'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me



html = urlopen("https://www.allrecipes.com/recipes/16492/everyday-cooking/special-collections/allrecipes-allstars/")
bsObj = BeautifulSoup(html.read())

allrecipes_urls = []

for link in bsObj.find_all('a'):
    if link is not None:
        allrecipes_urls.append(link.get('href', ''))

allrecipes_urls = [s for s in allrecipes_urls[3:] if 'https://www.allrecipes.com/recipe/' in s]

recipe_dict = {}
used_recipes = []

print(allrecipes_urls)

for recipe in allrecipes_urls:
    if recipe in used_recipes:
        pass
    else:
        scraper = scrape_me(recipe)
        recipe_info = {'title': scraper.title(), 'yields': scraper.yields(), 'ingredients': scraper.ingredients()
                       , 'instructions': scraper.instructions()}
        recipe_dict[scraper.title()] = recipe_info
        used_recipes.append(recipe)

        #recipe_dict[scraper.title()]['total_time'] = scraper.total_time()
        #recipe_dict[scraper.title()]['yields'] = scraper.yields()
        #recipe_dict[scraper.title()]['ingredients'] = scraper.ingredients()
        #recipe_dict[scraper.title()]['instructions'] = scraper.instructions()
        #recipe_dict[scraper.title()]['links'] = scraper.links()


print(recipe_dict)

