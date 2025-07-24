import requests
import json
query = input("What News U Want ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-17&sortBy=publishedAt&apiKey=27115d1bfed348bf9f0cc8639a581091"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------------------------------------------------------------------------------")