from asyncio import sleep
from tempfile import tempdir
from bs4 import BeautifulSoup
from requests import get
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36', "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "content-type": "application/x-www-form-urlencoded;charset=UTF-8", "sec-ch-ua-platform": "Windows"}

def results_data():
    details_data = []

    try:
        url = "https://drive.google.com/drive/folders/0BzL6M5WpOxAdUW1ON2RwWS1YZk0?%3Fsort=13&direction=a&resourcekey=0-8dUsMxL2N68MPYiPX3oQiw"
        page = get(url, headers=headers)
        page_contents = BeautifulSoup(page.content , "lxml")
        parent_container = page_contents.find("div", {"class": "iZmuQc"})

        data_containers = parent_container.find_all("div" ,{"jscontroller" : "LPQUTd"})

        for container in data_containers:
            print("*"*40)
            z = (container["data-id"])
            # print(z["data-id"])

            print(z)

        print(len(data_containers))
        
      
      
    except:
        print("error occurred")

results_data()
