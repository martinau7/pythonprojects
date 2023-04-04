from urllib.request import urlopen

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup

url = "https://chess-rankings.com/?country=Macedonia"
html = urlopen(url)
soup = BeautifulSoup(html)

allrows = soup.find_all("tbody", {"class": "contenidobusqueda"})

tbody = soup.find('tbody', {'class': 'contenidobusqueda'})
rows = tbody.find_all('tr')
data_pname = []
data_pelo = []
data_page = []
data_prank = []

for row in rows:
    player_id = row['id']
    name = row.find('td', {'class': 'nombre'}).text.strip()
    num = row.select('td:nth-of-type(6)')[0].text.strip()
    second_last_td = row.find_all('td')[-2].text.strip()
    data_pname.append(name)
    data_pelo.append(num)
    data_page.append(second_last_td)
    data_prank.append(num)

df = pd.DataFrame({'Name': data_pname, 'Chess Elo': data_pelo, 'Age': data_page, 'Player Ranking': data_prank})
print(df)

df['Chess Elo'] = pd.to_numeric(df['Chess Elo'], errors='coerce')
df['Player Ranking'] = pd.to_numeric(df['Player Ranking'], errors='coerce')

plt.scatter(df['Player Ranking'], df['Chess Elo'])
plt.xlabel('Player Ranking')
plt.ylabel('Chess Elo')
plt.title('Player Ranking vs Chess Elo')
plt.show()
