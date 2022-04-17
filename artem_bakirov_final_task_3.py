import pprint

import requests

currency_name = input("Enter your currency:").split(" ")
try:
    key = "8c7bbe5e8d1ff573a2eca963f9e861961478f1cb"
    parameters = {"api_key": key, "from": currency_name[0], "to": "UAH", "amount": 1}


    def change_money():
        if len(currency_name) == 1:
            url = "https://api.getgeoapi.com/v2/currency/convert"
            response = requests.get(url, parameters).json()
            print(str(currency_name))
            print(response["rates"]["UAH"]["rate"])
        else:
            new_url = f"https://api.getgeoapi.com/v2/currency/historical/{currency_name[1]}"
            response_date = requests.get(new_url, parameters).json()
            if response_date['status'] == "success":
                print(str(currency_name))
                print(response_date["rates"]["UAH"]["rate"])
            else:
                print(f"Invalid date: {currency_name[1]}")


    if __name__ == "__main__":
        change_money()
except KeyError:
    print(f"Invalid currency name: {str(currency_name[0])}")
except BaseException:
    print("System Error")
