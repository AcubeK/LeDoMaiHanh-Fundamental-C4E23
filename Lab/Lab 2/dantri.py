from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
#connect
url = "https://dantri.com.vn"
conn = urlopen(url)

#download
raw_data = conn.read()
page_content = raw_data.decode("utf8")  #or utf-8 to analizw special chararter


# with open("dantri.html", "wb") as f:
#     f.write(raw_data)

#find ROI region (Region of interest)
soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")       #href = "", id = ""
# print(ul.prettify())


#extract data
li_list = ul.find_all("li")
new_list = []
for li in li_list:
    a = li.h4.a
    # print(a.string)
    # print(a["href"])
    title = a.string
    link = url + a["href"]
    news ={
        "title" : title,
        "link" : link,
    }
    new_list.append(news)
    print(news)

#save data

# pyexcel.save_as(records = new_list, dest_file_name = "dantri.xlsx")