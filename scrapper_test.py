from bs4 import BeautifulSoup
import requests 

url = "https://www.pro-football-reference.com/teams/buf/2024.htm" 

web_page = requests.get(url)
doc = BeautifulSoup(web_page.text, "html.parser")

table = doc.find_all(["tbody"])[4] #the table where the data is located 
# print(tbody) # delete first hashtag to check the data table is captured

#trs = tbody.contents #the table rows of each player
# print(trs) # delete first hashtag to check the rows are captured

#for tr in trs:
 #   print(tr)

#print(table.find_all(["tr", "data-stat"]))

trs = table.find_all("tr")

for row in trs:
    cols = row.find_all("td")

    if cols:
        for td in cols:
            #print(td.text)
            data_text = td.text.strip() if td.text.strip() else 0
            print(data_text)

        print()
