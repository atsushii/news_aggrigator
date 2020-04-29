from ..contants import NEWS_URL
import requests
from bs4 import BeautifulSoup


class Scrape():

    def scrape_news(self):

        data_dict = {}

        # CBC news data
        page = requests.get(NEWS_URL["CBC"])

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, "lxml")

            flag = self.is_empty_scrap_data(soup.find_all("h3", class_="headline"), soup.find(
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
            flag = self.is_empty_scrap_data(soup.find("a", class_="vilynx_disabled"), soup.find(
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

            flag = self.is_empty_scrap_data(soup.find_all("h2"), soup.find(
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

            flag = self.is_empty_scrap_data(soup.find("a", class_="DY5T1d"),
                                            soup.find("a", class_="VDXfz"))
            if flag:
                data_dict["GOOGLE"] = {"Title": soup.find("a", class_="DY5T1d").string, "URL": "https://news.google.com" +
                                       soup.find("a", class_="VDXfz")["href"].split(".")[1]}
            else:
                data_dict["GOOGLE"] = {"Title": "", "URL": ""}

        return data_dict

    def is_empty_scrap_data(self, title, url):
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
