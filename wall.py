
import requests
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
# for i in range(100):
url = f"https://wallhaven.cc/hot?page={1}"
res = requests.get(url,headers=header)
print(res.text)