import requests


class AddressSeacher:
    def search(self, postal_code):
        url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
        response = requests.get(url)
        response_dict = response.json()
        都道府県 = response_dict["results"][0]["address1"]
        市区町村 = response_dict["results"][0]["address2"]
        町域 = response_dict["results"][0]["address3"]
        return f"{都道府県}{市区町村}{町域}"
