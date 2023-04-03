from urllib.request import urlopen

from bs4 import BeautifulSoup

url = "https://chess-rankings.com/?country=Macedonia"
html = urlopen(url)
soup = BeautifulSoup(html)

allrows = soup.find_all("tbody", {"class": "contenidobusqueda"})

tbody = soup.find('tbody', {'class': 'contenidobusqueda'})
rows = tbody.find_all('tr')

for row in rows:
    player_id = row['id']
    name = row.find('td', {'class': 'nombre'}).text.strip()
    num = row.select('td:nth-of-type(6)')[0].text.strip()
    second_last_td = row.find_all('td')[-2].text.strip()
    print(f"Player Rank: {player_id}")
    print(f"Player Name: {name}")
    print(f"Player Chess Elo: {num}")
    print(f"Player Age: {second_last_td}")
    print("_____________________________")
