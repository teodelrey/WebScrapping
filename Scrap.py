# importamos bibliotecas
from bs4 import BeautifulSoup
import request
import pandas as pd

# almacenamos la url en una variable
url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = request.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos    

eq = soup.find_all('span', class_="nombre-equipo")

print(eq)