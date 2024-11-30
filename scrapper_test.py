from qb_obj import QB_Player
from player_obj import Player
from bs4 import BeautifulSoup
import requests 

url = "https://www.pro-football-reference.com/teams/buf/2024.htm" 

web_page = requests.get(url)
doc = BeautifulSoup(web_page.text, "html.parser")

## BUFFALO BILLS
buffalo_bills_players = []

# QB TABLE STATS FOR PASSING

QB_table = doc.find_all(["tbody"])[3]
QB_trs = QB_table.find_all("tr")

# col 0 = name, col 3 = games played, col 6 = completions, col 7 = attempts, col 9 = yards
# col 10 = tds, col 12 = interceptions
for row in QB_trs:
    cols = row.find_all('td')
    if int(cols[7].text.strip()) > 50: # this is a filter to exclude QBs that didnt play very much
        QB = QB_Player(cols[0].text.strip(), "QB", cols[3].text.strip(), cols[6].text.strip(), cols[7].text.strip(), cols[9].text.strip(), cols[10].text.strip(), cols[12].text.strip())
        buffalo_bills_players.append(QB);

# THE TABLE FOR RUSHING AND RECEIVING STATS

table = doc.find_all(["tbody"])[4] #the table where the data is located 
trs = table.find_all("tr")

#col 0 = name, col 2 = position, col 3 = games played, col 5 = rush attempts, 
# col 6 = rush yards, col 7 = rush TD, col 14 = rec tgts, col 15 = receptions, col 16 = rec yards, col 18 = rec TDs
for row in trs:
    cols = row.find_all("td")

    if (str(cols[2].text.strip()) == "QB"):
        for player in buffalo_bills_players:
            if player.name == str(cols[0].text.strip()):
                player.rushing_attempt = cols[5].text.strip()
                player.rush_yards = cols[6].text.strip()
                player.rush_td = cols[7].text.strip()
    elif (int(cols[15].text.strip()) >= 10 or int(cols[5].text.strip()) > 25):
        player = Player(cols[0].text.strip(), cols[2].text.strip(), cols[3].text.strip(), cols[5].text.strip(), cols[6].text.strip(), cols[7].text.strip(), cols[14].text.strip(), cols[15].text.strip(), cols[16].text.strip(), cols[18].text.strip())
        buffalo_bills_players.append(player)

for playa in buffalo_bills_players:
    playa.print_stats()
