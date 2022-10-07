import urllib.request as req
goodList=[]
ordinList=[] 
badList=[] 
def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36})"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import sys
    sys.path.append("d:\\anaconda3\lib\site-packages")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")   #從網頁中尋找標籤，尋找 class="title"的div標籤， _all 尋找所有符合條件的標籤
    
      
    for title in titles:
        if title.a != None and title.a.string[0:4]=="[好雷]":
            goodList.append(title.a.string)
    
    for title in titles:
        if title.a != None and title.a.string[0:4]=="[普雷]":
            ordinList.append(title.a.string)

    for title in titles:
        if title.a != None and title.a.string[0:4]=="[負雷]":
            badList.append(title.a.string)
    
    #抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁")    #找到內文是‹ 上頁的a標籤;用bs4根據條件(內文:String)去找到我們想要的標籤
    return (nextLink["href"])   #目標是這個標籤的屬性 href


#主程序：抓取多個頁面標題;使用while迴圈抓多頁
pageUrl="https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<10:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1

movieList=goodList+ordinList+badList
# print(movieList)
with open("movie.txt", "w", encoding='UTF-8') as file:
    for movie in movieList:
        file.write(movie+"\n")


