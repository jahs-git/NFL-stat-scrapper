from bs4 import BeautifulSoup
import requests 

url = "https://www.pro-football-reference.com/teams/buf/2024.htm" 

web_page = requests.get(url)
doc = BeautifulSoup(web_page.text, "html.parser")

tags = doc.find_all(["tbody"])[4] #the table where the data is located 

print(tags)
