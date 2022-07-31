from   utils.scrap_data import ScrapData



class DriveData():
    def drive_details( url = "https://drive.google.com/drive/folders/0B3B3M4Atq6YeWHUyNjktTlRaR1E?resourcekey=0-kPsEBf9AFX5JzHulg-mbDA"):
        """Insert link of drive to get its files data"""

        data_ary = []
        id = 0


        try:
            page_contents = ScrapData.scrap(url)
            parent_container = page_contents.find("div", {"class": "iZmuQc"})

            data_containers = parent_container.find_all("div" ,{"jscontroller" : "LPQUTd"})

            # for x in data_containers:
            #     print(x)
            #     print("-"  *100)
            # direct_download = DriveData.drive_download_link()

            for container in data_containers:
                video_i = container["data-id"]
                link_dow = f"https://drive.google.com/uc?id={video_i}&export=download"
                direct_url = "https://drive.google.com/file/d/" + str(container["data-id"])
                container_data = {
                    "id": id,
                    "video_id": container["data-id"],
                    "title": (container.find("div", {"class": "Q5txwe"}).string),
                    "download_link": link_dow,
                    "direct_url": direct_url
                }
                data_ary.append(container_data)
                id += 1
        
            return data_ary

        except Exception as e:
            return e



    def drive_download_link(link=''):
        """Insert google drive download page link to get download link"""\

        try:
            page_contents = ScrapData.scrap(link)
            download_tag = page_contents.find("form", {"id" : "downloadForm"})
            download_link = download_tag["action"]

            return download_link

        except Exception as e:
            return e;


# print(DriveData.drive_details("https://drive.google.com/drive/folders/0B3B3M4Atq6YeWHUyNjktTlRaR1E?resourcekey=0-kPsEBf9AFX5JzHulg-mbDA"))
# print(DriveData.search_results("movies"))