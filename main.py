from bs4 import BeautifulSoup
import requests

website = "https://www.allrecipes.com/search/results/"
# Pretending you are legit
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

ingredients_remaining = True
ingredients = []

while ingredients_remaining:
    ingredients.append(input("Tell me something that's in your fridge "))
    more = input("Anything else in your fridge? Type Yes or No ").title()
    if more != "Yes":
        ingredients_remaining = False


query = f"?IngIncl={ingredients[0]}"
for ingredient in ingredients[1:]:
    query += f"&IngIncl={ingredient}"

endpoint = website + query

response = requests.get(url=endpoint, headers=headers)
response.raise_for_status()

recipe_webpage = response.text

soup = BeautifulSoup(recipe_webpage, "html.parser")



recipe_titles = [link["title"] for link in soup.find_all(class_="elementFont__titleLink")]
recipe_descriptions = [description.get_text().replace("\n","").strip() for description in soup.find_all(class_="elementFont__details--paragraphWithin")]
recipe_links = [link["href"] for link in soup.find_all(class_="elementFont__titleLink")]


