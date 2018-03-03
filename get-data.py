import os
import urllib2
from bs4 import BeautifulSoup

links = []
page = open("links.txt", "r").read()

page = BeautifulSoup(page)
t =  page.find_all("li", class_ = "marg-b-1")

for li in t:
    links.append(li.a.attrs["href"])
    #print li.a.attrs["href"]


start = int(raw_input("Start from: "))
end = int(raw_input("End value: "))

os.system("mkdir files")

for i in range(start, end+1):
    os.system("wget -P ./files \""+str(links[i])+ "\"")
