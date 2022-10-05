import urllib.request as request
import json
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

sight_list=data["result"]["results"]

with open('data.csv', 'w') as file:
    
    writer = csv.writer(file)
    
    for brief_info in sight_list:
        pic_position=brief_info["file"].index("http", brief_info["file"].index("http")+1)
        date_year=brief_info["xpostDate"][0:4]
        if date_year>="2015":
            brief_info = [brief_info["stitle"], brief_info["address"][5:8], brief_info["longitude"], brief_info["latitude"], brief_info["file"][0:pic_position]]
            writer.writerow(brief_info)


# with open("dataA.txt", "w", encoding="utf-8") as file:
#     for brief_info in sight_list:
#         date_year=brief_info["xpostDate"][0:4]
#         if date_year>="2015":
#             #print(brief_info["stitle"]+","+brief_info["address"][5:8]+","+brief_info["longitude"]+","+brief_info["latitude"]+","+adj_pic_url)
#             file.write(brief_info["stitle"]+","+brief_info["address"][5:8]+","+brief_info["longitude"]+","+brief_info["latitude"]+","+adj_pic_url)

#把變數串成一個字串再一起 write 出去
#使用csv格式

# for sight_name in sight_list:
#     sight_name=sight_name["stitle"]


# for district in sight_list:
#     district=district["address"][5:8]
#     #print(district)

# for longitude in sight_list:
#     longitude=longitude["longitude"]
#     #print(longitude)

# for latitude in sight_list:
#     latitude=latitude["latitude"]
#     #print(latitude)

# for pic_url in sight_list:
#     pic_url=pic_url["file"]
#     pic_position=pic_url.index("http", pic_url.index("http")+1)
#     adj_pic_url=pic_url[0:pic_position]
    #print(adj_pic_url)