from bs4 import BeautifulSoup
from requests import get

class ScrapData():

    def scrap(site_link  = ""):
        """Enter link of webpage to extract html"""

        try:
            site = get(site_link )
            page_connect = BeautifulSoup(site.content, "html.parser")
            return page_connect

        except Exception as e:
            return e


# print(ScrapData.scrap())

