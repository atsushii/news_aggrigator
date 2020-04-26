import requests
from bs4 import BeautifulSoup
from app.models import News
from app.contants import NEWS_URL
from flask import Blueprint

view_blueprint = Blueprint("view_blueprint", __name__)
@view_blueprint.route('/hello')
def scrape_data():
    """
    scraping data from news page
    """

    # dictionary of news data(title, url)
    data_dict = {}

    # CBC news data
    page = requests.get(NEWS_URL["CBC"])

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "lxml")

        flag = is_empty_scrap_data(soup.find_all("h3", class_="headline"), soup.find(
            "a", class_="primaryHeadlineLink sclt-contentpackageheadline"))
        if flag:
            data_dict["CBC"] = {"Title": soup.find_all("h3", class_="headline")[0].string, "URL": "https://www.cbc.ca" +
                                soup.find("a", class_="primaryHeadlineLink sclt-contentpackageheadline")["href"]}
        else:
            data_dict["CBC"] = {"Title": "", "URL": ""}

    # NBC news data
    page = requests.get(NEWS_URL["NBC"])

    if page.status_code == 200:

        soup = BeautifulSoup(page.content, "lxml")

        flag = is_empty_scrap_data(soup.find("a", class_="vilynx_disabled"), soup.find(
            "a", class_="vilynx_disabled")["href"])

        if flag:

            data_dict["NBC"] = {"Title": soup.find("a", class_="vilynx_disabled").string, "URL": soup.find(
                "a", class_="vilynx_disabled")["href"]}
        else:
            data_dict["NBC"] = {"Title": "", "URL": ""}

    # YAHOO news data
    page = requests.get(NEWS_URL["YAHOO"])

    if page.status_code == 200:

        soup = BeautifulSoup(page.content, "lxml")

        flag = is_empty_scrap_data(soup.find_all("h2"), soup.find(
            id="item-0").find("a", class_="Td(n)"))

        if flag:

            data_dict["YAHOO"] = {"Title": soup.find_all("h2")[1].string, "URL": "https://ca.news.yahoo.com" +
                                  soup.find(id="item-0").find("a", class_="Td(n)")["href"]}
        else:
            data_dict["YAHOO"] = {"Title": "", "URL": ""}

    # GOOGLE news data
    page = requests.get(NEWS_URL["GOOGLE"])

    if page.status_code == 200:

        soup = BeautifulSoup(page.content, "lxml")

        flag = is_empty_scrap_data(soup.find("a", class_="DY5T1d"),
                                   soup.find("a", class_="VDXfz"))
        if flag:
            data_dict["GOOGLE"] = {"Title": soup.find("a", class_="DY5T1d").string, "URL": "https://news.google.com" +
                                   soup.find("a", class_="VDXfz")["href"].split(".")[1]}
        else:
            data_dict["GOOGLE"] = {"Title": "", "URL": ""}

    return data_dict


def is_empty_scrap_data(title, url):
    """
    check empty scrape data 
    if empty can't read that data from db

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
