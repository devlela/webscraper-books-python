import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

livros = soup.find_all("h3")
for livro in livros:
    print(livro.a["title"])
