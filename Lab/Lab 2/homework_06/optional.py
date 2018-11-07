from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

rawdata = conn.read()
page_content = rawdata.decode()
soup = BeautifulSoup(page_content, "html.parser")

div = soup.find("div", id="divTableHeader")
col_list = div.find_all("td", "h_t")
columns = [""]

for col in col_list:
    a = str(col.string).replace("\r\n                    ", "")
    columns.append(a)

table = soup.find("table", id = "tableContent")
tr_list = table.find_all("td", "b_r_c")
rows = []
for tr in tr_list:
    a = str(tr.string)
    b = a.replace("\r\n                \xa0\xa0\r\n                ", "")
    c = b.replace("\r\n            ", "").replace("    \xa0\xa0\xa0\xa0      ", "")
    rows.append(c)

for i in range(len(rows)+1, -1, -1): 
    if (i+1)%(len(columns)+1) == 0:                      #ask
        rows.pop(i)

x = 0
y = len(rows)/len(columns)-1
table = []
while x <= y:
    data ={}
    for i in range(len(columns)):
        data[columns[i]] = rows[i+len(columns)*x]
    table.append(data)
    x+=1

pyexcel.save_as(records = table, dest_file_name = "economy.xlsx")




