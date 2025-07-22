import requests
from bs4 import BeautifulSoup

url = "https://abhishekportpandey.netlify.app/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)