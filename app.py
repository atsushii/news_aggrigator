from flask import Flask
import requests
from bs4 import BeautifulSoup


def batch():
    """
    batch procces, scraping data from news page
    """
    URL_CBC = "https://www.cbc.ca/news"
    page = requests.get(URL_CBC)
    soup = BeautifulSoup(page.content, "lxml")
    print("title", soup.find_all("h3", class_="headline")[0].string)
    print("url", "https://www.cbc.ca" +
          soup.find("a", id="m-card-1.5529020")["href"])

    URL_NBC = "https://www.nbcnews.com/"
    page = requests.get(URL_NBC)
    soup = BeautifulSoup(page.content, "lxml")
    print("title", soup.find("a", class_="vilynx_disabled").string)
    print("url", soup.find("a", class_="vilynx_disabled")["href"])

    URL_YAHOO = "https://ca.news.yahoo.com/"
    page = requests.get(URL_YAHOO)
    soup = BeautifulSoup(page.content, "lxml")
    print("title", soup.find_all("h2")[1].string)
    print("url", "https://ca.news.yahoo.com" +
          soup.find(id="item-0").find("a", class_="Td(n)")["href"])

    app = Flask(__name__)
    URL_GOOGLE = "https://news.google.com/"
    page = requests.get(URL_GOOGLE)
    soup = BeautifulSoup(page.content, "lxml")
    print("title", soup.find("a", class_="DY5T1d").string)
    print("url", "https://news.google.com" +
          soup.find("a", class_="VDXfz")["href"].split(".")[1])
