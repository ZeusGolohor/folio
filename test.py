#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
from models.web_page_monitor import WebPageMonitor

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")
# #print(soup.prettify())

# url = 'https://www.livescores.com/football/egypt/premier-league/?tz=-7'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# target_class = soup.find("div", class_="na")  # Replace "div" with the actual tag and "my-class" with your target class name
# print(target_class.prettify())

# with open("./livescores/LiveScore_Football_Premier_League_Live_Football_Scores_Egypt.html", 'r') as fp:
# #   soup = BeautifulSoup(fp, features="html.parser")
#   soup = BeautifulSoup(fp, features="lxml")
#   print(soup.prettify())

with open("./livescores/LiveScore_Football_Premier_League_Live_Football_Scores_Egypt.html", 'r') as fp:
  monitor = WebPageMonitor()
  file = {'fp': fp}
  monitor.init_BeautifulSoup(**file)
  print(monitor.select_sport())


