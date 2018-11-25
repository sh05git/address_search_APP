from address_seacher import AddressSeacher


def main():
    pass

    # ユーザーからの郵便番号の入力を受け取る
    postal_code = input("郵便番号は？> ")

    # 郵便番号を使って地名を取ってくる
    address_searcher = AddressSeacher()

    location = address_searcher.search(postal_code)

    # 地名をprintする
    print(location)


if __name__ == "__main__":
    main()
