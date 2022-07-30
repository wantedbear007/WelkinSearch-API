from bs4 import BeautifulSoup
from requests import get


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36', "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "content-type": "application/x-www-form-urlencoded;charset=UTF-8", "sec-ch-ua-platform": "Windows"}


def archive_details(url = "https://drive.google.com/drive/folders/1nt9zQMq7ZKlN-1fmwHGqy_q5ckygzEXk"):
    details_data = []

    try:
        page = get(url, headers=headers)
        page_contents = BeautifulSoup(page.content , "html.parser")
        parent_container = page_contents.find("div", {"class": "iZmuQc"})
        data_containers = parent_container.find_all("div" ,{"jscontroller" : "LPQUTd"})
        id = 0

        # # TESTING PHASE 

        # trial_data = page_contents.find("div", class_="VIrDCd")

        # # TESTING PHASE
        # print(len(trial_data))
        # # lol = trial_data.find_all("div", class_="WYuW0e")
        # lol = trial_data.find_all("div", class_="jGNTYb ACGwFc")

        # for l in lol:

        #     print(l)
        #     print("-" * 100)

        # print(len(lol))
        # print(data_containers)
        # print(len(data_containers))

        for x in data_containers:
            print(x)
            print("-"  *100)



      
# NOTICE 
# EXTRACT DOWNLOAD LINK FROM DOWNLOAD PAGE 

        for container in data_containers:
            video_i = container["data-id"]
            link_dow = f"https://drive.google.com/uc?id={video_i}&export=download"
            container_data = {
                "id": id,
                "video_id": container["data-id"],
                "title": (container.find("div", {"class": "Q5txwe"}).string),
                "download_link": link_dow,
                "direct_url": "https://drive.google.com/file/d/" + str(container["data-id"])
            }
            details_data.append(container_data)
            id += 1
        
        return details_data

      
    except BaseException  as e:
        
        return e.message




archive_details("https://drive.google.com/drive/folders/0B3B3M4Atq6YeWHUyNjktTlRaR1E?resourcekey=0-kPsEBf9AFX5JzHulg-mbDA")

# print(archive_details())
