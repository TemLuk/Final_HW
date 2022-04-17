import requests
city_name = input("Enter your city:").lower()
try:
    def response_func():
        api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
        first_response = requests.get(api_url, headers={'X-Api-Key': "ixZwtSSbYFrVDZo3KaeA+Q==pRB0axCv4X0berXl"}).json()
        return first_response

    while not response_func():
        print(f"Invalid city name:{city_name}")
        city_name = input("Enter correct city:")

    def get_population():
        return response_func()[0]['population']

    def get_country():
        return response_func()[0]['country']

    def get_currency():
        url = "https://api.api-ninjas.com/v1/country?name={}".format(get_country())
        second_response = requests.get(url, headers={'X-Api-Key': "ixZwtSSbYFrVDZo3KaeA+Q==pRB0axCv4X0berXl"}).json()
        return second_response[0]['currency']['code']

    print(get_country())
    print(get_currency())
    print(get_population())

except BaseException:
    print("System Error")


