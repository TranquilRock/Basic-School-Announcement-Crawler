import urllib.request as req
url="https://www.csie.ntu.edu.tw/news/news.php?class=101"
request=req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
#print(root.title.string)
titles=root.find_all("tr")
for even in titles:
    
    if even.td!=None:
        print(even.td.string)
        print(even.a.string)
        print("\n")
