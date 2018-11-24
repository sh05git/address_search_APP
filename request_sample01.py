import requests

# response = requests.get(url="http://hachimantai.spartacamp.jp/")

response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")
print(response)

response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=8150074")
print(response)
