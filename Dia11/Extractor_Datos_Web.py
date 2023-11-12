import bs4
import requests
import lxml

resultado = requests.get('https://escueladirecta-blog.blogspot.com')
sopa = bs4.BeautifulSoup(resultado.text, ' lxml')

print(sopa.select('title') [0].getText())

columna_lateral = sopa.select(' .contemt p')
print(columna_lateral)