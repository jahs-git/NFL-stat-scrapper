from qb_obj import QB_Player
from player_obj import Player
from bs4 import BeautifulSoup
import requests 


teams = []
#AFC EAST
teams.append(("BUFFALO BILLS", "https://www.pro-football-reference.com/teams/buf/2024.htm", []))
teams.append(("MIAMI DOLPHINS" , "https://www.pro-football-reference.com/teams/mia/2024.htm", []))
teams.append(("NEW YORK JETS", "https://www.pro-football-reference.com/teams/nyj/2024.htm", []))
teams.append(("NEW ENGLAND PATRIOTS", "https://www.pro-football-reference.com/teams/nwe/2024.htm", []))
#AFC SOUTH
teams.append(("HOUSTON TEXANS", "https://www.pro-football-reference.com/teams/htx/2024.htm", []))
teams.append(("INDIANAPOLIS COLTS", "https://www.pro-football-reference.com/teams/clt/2024.htm" ,[]))
teams.append(("TENNESE TITANS", "https://www.pro-football-reference.com/teams/oti/2024.htm", []))
teams.append(("JACKSONVILLE JAGUARS" , "https://www.pro-football-reference.com/teams/jax/2024.htm", []))
#AFC NORTH
teams.append(("PITTSBURG STEELERS", "https://www.pro-football-reference.com/teams/pit/2024.htm", []))
teams.append(("BALTIMORE RAVENS", "https://www.pro-football-reference.com/teams/rav/2024.htm", []))
teams.append(("CINCINNATI BENGALS", "https://www.pro-football-reference.com/teams/cin/2024.htm", []))
teams.append(("CLEVELAND BROWNS", "https://www.pro-football-reference.com/teams/cle/2024.htm", []))
#AFC WEST
teams.append(("KANSAS CHEIFS", "https://www.pro-football-reference.com/teams/kan/2024.htm", []))
teams.append(("LOS ANGELES CHARGERS", "https://www.pro-football-reference.com/teams/sdg/2024.htm", []))
teams.append(("DENVER BRONCOS", "https://www.pro-football-reference.com/teams/den/2024.htm", []))
teams.append(("LOS VEGAS RAIDERSS", "https://www.pro-football-reference.com/teams/rai/2024.htm", []))
#NFC EAST
teams.append(("PHILADELPHIA EAGLES", "https://www.pro-football-reference.com/teams/phi/2024.htm", []))
teams.append(("WASHINGTON COMMANDERS", "https://www.pro-football-reference.com/teams/was/2024.htm", []))
teams.append(("DALLAS COWBOYS", "https://www.pro-football-reference.com/teams/dal/2024.htm", []))
teams.append(("NEW YORK GIANTS", "https://www.pro-football-reference.com/teams/nyg/2024.htm", []))
#NFC SOUTH
teams.append(("ATLANTA FALCONS", "https://www.pro-football-reference.com/teams/atl/2024.htm", []))
teams.append(("TAMPA BAY BUCCANEERS", "https://www.pro-football-reference.com/teams/tam/2024.htm", []))
teams.append(("NEW ORLEAN SAINTS", "https://www.pro-football-reference.com/teams/nor/2024.htm", []))
teams.append(("CAROLINA PANTHERS", "https://www.pro-football-reference.com/teams/car/2024.htm", []))
#NFC NORTH
teams.append(("DETROIT LIONS", "https://www.pro-football-reference.com/teams/det/2024.htm", []))
teams.append(("MINNESOTA VIKINGS", "https://www.pro-football-reference.com/teams/min/2024.htm", []))
teams.append(("GREENBAY PACKERS", "https://www.pro-football-reference.com/teams/gnb/2024.htm", []))
teams.append(("CHICAGO BEARS", "https://www.pro-football-reference.com/teams/chi/2024.htm", []))
#NFC WEST
teams.append(("ARIZONA CARDINALS", "https://www.pro-football-reference.com/teams/crd/2024.htm", []))
teams.append(("SEATTLE SEAHAWKS", "https://www.pro-football-reference.com/teams/sea/2024.htm", []))
teams.append(("LOS ANGELES RAMS", "https://www.pro-football-reference.com/teams/ram/2024.htm", []))
teams.append(("SAN FRANCISCO 49ers", "https://www.pro-football-reference.com/teams/sfo/2024.htm", []))

for team in teams:
    url = team[1] 
    web_page = requests.get(url)
    doc = BeautifulSoup(web_page.text, "html.parser")
    team_players = []
    #QB TABLE STATS FOR PASSING
    print(team[0])
    QB_table = doc.find_all(["tbody"])[3]
    QB_trs = QB_table.find_all("tr")
    # col 0 = name, col 3 = games played, col 6 = completions, col 7 = attempts, col 9 = yards
    # col 10 = tds, col 12 = interceptions
    for row in QB_trs:
       cols = row.find_all('td')
       if int(cols[7].text.strip()) > 50: # this is a filter to exclude QBs that didnt play very much
            QB = QB_Player(cols[0].text.strip(), "QB", cols[3].text.strip(), cols[6].text.strip(), cols[7].text.strip(), cols[9].text.strip(), cols[10].text.strip(), cols[12].text.strip())
            team[2].append(QB);

# THE TABLE FOR RUSHING AND RECEIVING STATS

    table = doc.find_all(["tbody"])[4] #the table where the data is located 
    trs = table.find_all("tr")

#col 0 = name, col 2 = position, col 3 = games played, col 5 = rush attempts, 
# col 6 = rush yards, col 7 = rush TD, col 14 = rec tgts, col 15 = receptions, col 16 = rec yards, col 18 = rec TDs
    for row in trs:
        cols = row.find_all("td")

        if (str(cols[2].text.strip()) == "QB"):
            for player in team[2]:
                if player.name == str(cols[0].text.strip()):
                    player.rushing_attempt = cols[5].text.strip()
                    player.rush_yards = cols[6].text.strip()
                    player.rush_td = cols[7].text.strip()
                    
        elif (int(cols[15].text.strip()) >= 10 or int(cols[5].text.strip()) > 25):
            player = Player(cols[0].text.strip(), cols[2].text.strip(), cols[3].text.strip(), cols[5].text.strip(), cols[6].text.strip(), cols[7].text.strip(), cols[14].text.strip(), cols[15].text.strip(), cols[16].text.strip(), cols[18].text.strip()) 
            team[2].append(player)



player_list = []

for team_name, team_link, players in teams:
    print("====================")
    print(team_name)
    print("====================")

    for playa in players:
        #player_list.append((player.name(), team_name()))
        playa.print_stats()
#for player_name, team_name in player_list:
    #print(player_name, team_name)

#def full_team_stats(user_team_name):
    #for team_name, team_link, players in teams:
        #if(team_name.lower() == user_team_name):
           #for player in team:
                #player.print_stats()


#user_input = input("enter team name to display stats: ")
#full_team_stats(user_input.lower())


