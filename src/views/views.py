import requests
from bs4 import BeautifulSoup
from ..models import News


def scrape_data():
    """
    scraping data from news page
    """

    # dictionary of news data(title, url)
    data_dict = {}

    # CBC news data
    URL_CBC = "https://www.cbc.ca/news"
    page = requests.get(URL_CBC)
    soup = BeautifulSoup(page.content, "lxml")

    flag = validation_data(soup.find_all("h3", class_="headline"), soup.find(
        "a", class_="primaryHeadlineLink sclt-contentpackageheadline"))
    if flag:
        data_dict["CBC"] = {"Title": soup.find_all("h3", class_="headline")[0].string, "URL": "https://www.cbc.ca" +
                            soup.find("a", class_="primaryHeadlineLink sclt-contentpackageheadline")["href"]}
    else:
        data_dict["CBC"] = {"Title": "No title", "URL": "No url"}

    # NBC news data
    URL_NBC = "https://www.nbcnews.com/"
    page = requests.get(URL_NBC)
    soup = BeautifulSoup(page.content, "lxml")

    flag = validation_data(soup.find("a", class_="vilynx_disabled"), soup.find(
        "a", class_="vilynx_disabled")["href"])

    if flag:

        data_dict["NBC"] = {"Title": soup.find("a", class_="vilynx_disabled").string, "URL": soup.find(
            "a", class_="vilynx_disabled")["href"]}
    else:
        data_dict["NBC"] = {"Title": "No title", "URL": "No url"}

    # YAHOO news data
    URL_YAHOO = "https://ca.news.yahoo.com/"
    page = requests.get(URL_YAHOO)
    soup = BeautifulSoup(page.content, "lxml")

    flag = validation_data(soup.find_all("h2"), soup.find(
        id="item-0").find("a", class_="Td(n)"))

    if flag:

        data_dict["YAHOO"] = {"Title": soup.find_all("h2")[1].string, "URL": "https://ca.news.yahoo.com" +
                              soup.find(id="item-0").find("a", class_="Td(n)")["href"]}
    else:
        data_dict["YAHOO"] = {"Title": "No title", "URL": "No url"}

    # GOOGLE news data
    URL_GOOGLE = "https://news.google.com/"
    page = requests.get(URL_GOOGLE)
    soup = BeautifulSoup(page.content, "lxml")

    flag = validation_data(soup.find("a", class_="DY5T1d"),
                           soup.find("a", class_="VDXfz"))
    if flag:
        data_dict["GOOGLE"] = {"Title": soup.find("a", class_="DY5T1d").string, "URL": "https://news.google.com" +
                               soup.find("a", class_="VDXfz")["href"].split(".")[1]}
    else:
        data_dict["GOOGLE"] = {"Title": "No title", "URL": "No url"}


def validation_data(title, url):
    """
    Validate scrape data

    title: str, news title
    url: str, news url

    return bool
    """

    if title and url:
        return True
    else:
        return False


def add_data_to_db(news_data):
    """
    add latest news data to db

    news_data: dict, latest news data
    """
    news_list = News.get_news_data()
    if news_list:
        News.delete_news_data(news_list)

    News.register_news_data(news_data)
