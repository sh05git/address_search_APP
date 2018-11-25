import requests


def main():
    # ユーザーからの郵便番号の入力を受け取る
    postal_code_input = input("郵便番号(半角数字で7桁)を入力してください: ")

    # 郵便番号を使って地名を取ってくる
    base_url = "http://zipcloud.ibsnet.co.jp/api/search"
    url = f"{base_url}?zipcode={postal_code_input}"

    response = requests.get(url)
    response_dict = response.json()

    都道府県 = response_dict["results"][0]["address1"]
    市区町村 = response_dict["results"][0]["address2"]
    町域 = response_dict["results"][0]["address3"]

    return f"{都道府県}{市区町村}{町域}"
    # 地名をprintする


if __name__ == "__main__":
    print(main())
