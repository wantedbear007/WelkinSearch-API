# WelkinSearch-API


### Features

- To search files

      https://welkin-search-api.vercel.app/search/{keyword}`
	  
	  //eg https://welkin-search-api.vercel.app/search/movies  `
	  
	  
    
   Returns
   ```JSON

  
    {
        "id": 0,
        "title": "Movies - Google Drive",
        "link": "https://drive.google.com/drive/folders/1nt9zQMq7ZKlN-1fmwHGqy_q5ckygzEXk",
        "path": " › drive › folders"
    },
    {
        "id": 1,
        "title": "ANIME & KIDS MOVIES - Google Drive",
        "link": "https://drive.google.com/drive/folders/0Bwq4CzEOZmxtVEt6bjdiaWJ2RTQ",
        "path": " › drive › folders"
    },
    {
        "id": 2,
        "title": "Watch Online Free HD Movies And Series - Google Drive",
        "link": "https://drive.google.com/drive/folders/17DnsqDmrhEQBA-uhrcIKdBIxV63hwUoP?usp=sharing",
        "path": " › drive › folders"
    },
    {
        "id": 3,
        "title": "Christmas Movies - Google Drive – Cloud Storage",
        "link": "https://drive.google.com/drive/folders/0B1j88lrqI04bUzQ5MUlpanhDMlk",
        "path": " › drive › folders"
    },


   ```
   
 - To get get specific drive files 
 
   ```
   
   Example
   
   POST REQUEST TO BELOW LINK
   eg https://welkin-search-api.vercel.app/drive
   
   WITH JSON BODY AS (link recieved from above request)
   {
    "link": "https://drive.google.com/drive/folders/0B3B3M4Atq6YeWHUyNjktTlRaR1E?resourcekey=0-kPsEBf9AFX5JzHulg-mbDA"
   }
   
   ```
   
   Returns
   



  ```JSON
  {
        "id": 0,
        "video_id": "0B3B3M4Atq6YeSFJMX2o0UGZaOUE",
        "title": "3 Hari Untuk Selamanya 2007.mp4",
        "download_link": "https://drive.google.com/uc?id=0B3B3M4Atq6YeSFJMX2o0UGZaOUE&export=download",
        "direct_url": "https://drive.google.com/file/d/0B3B3M4Atq6YeSFJMX2o0UGZaOUE"
    },
    {
        "id": 1,
        "video_id": "0B3B3M4Atq6YeSXlLN28yZm53Ymc",
        "title": "Alien_ Covenant Subtitle Indonesia.MP4",
        "download_link": "https://drive.google.com/uc?id=0B3B3M4Atq6YeSXlLN28yZm53Ymc&export=download",
        "direct_url": "https://drive.google.com/file/d/0B3B3M4Atq6YeSXlLN28yZm53Ymc"
    },
    {
        "id": 2,
        "video_id": "0B3B3M4Atq6Yed1FTdXFhZnZ1Nnc",
        "title": "Assassins _#8211; Nonton Film Bioskop Online.MP4",
        "download_link": "https://drive.google.com/uc?id=0B3B3M4Atq6Yed1FTdXFhZnZ1Nnc&export=download",
        "direct_url": "https://drive.google.com/file/d/0B3B3M4Atq6Yed1FTdXFhZnZ1Nnc"
    },
    {
        "id": 3,
        "video_id": "0B3B3M4Atq6YeS2xGTm9DWERfcTg",
        "title": "bandicam 2017-06-11 14-02-53-604.mp4",
        "download_link": "https://drive.google.com/uc?id=0B3B3M4Atq6YeS2xGTm9DWERfcTg&export=download",
        "direct_url": "https://drive.google.com/file/d/0B3B3M4Atq6YeS2xGTm9DWERfcTg"
    },
  
  ```
   

