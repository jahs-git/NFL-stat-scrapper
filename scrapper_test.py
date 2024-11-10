from bs4 import BeautifulSoup
import requests 

url = "https://www.pro-football-reference.com/teams/buf/2024.htm" 

web_page = requests.get(url)
doc = BeautifulSoup(web_page.text, "html.parser")

tbody = doc.find_all(["tbody"])[4] #the table where the data is located 
# print(tbody) # delete first hashtag to check the data table is captured

trs = tbody.contents #the table rows of each player
# print(trs) # delete first hashtag to check the rows are captured

for tr in trs:
    print(tr)
