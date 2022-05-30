from bs4 import BeautifulSoup
from requests import get


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36', "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "content-type": "application/x-www-form-urlencoded;charset=UTF-8", "sec-ch-ua-platform": "Windows"}


def drive_files(url):
    details_data = []

    try:
        page = get(url, headers=headers)
        page_contents = BeautifulSoup(page.content , "html.parser")
        parent_container = page_contents.find("div", {"class": "iZmuQc"})
        data_containers = parent_container.find_all("div" ,{"jscontroller" : "LPQUTd"})
        id = 0


        for container in data_containers:
            container_data = {
                "id": id,
                "video_id": container["data-id"],
                "title": (container.find("div", {"class": "Q5txwe"}).string)
            }
            details_data.append(container_data)
            id += 1
        
        return details_data

      
    except IndexError  as e:
        return e




# print(results_data("https://drive.google.com/file/d/0B4Sey0q2VOKNVDhkdE1vajZrMWc"))
