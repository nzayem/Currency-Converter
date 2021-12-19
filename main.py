import requests

user_agent = {'User-Agent': 'Mozilla/5.0'}
cache_currency = {}

# Initializing cache with USD and EUR:

url = "http://www.floatrates.com/daily/usd.json"
r = requests.get(url, headers=user_agent)
cache_currency['usd'] = r.json()

url = "http://www.floatrates.com/daily/eur.json"
r = requests.get(url, headers=user_agent)
cache_currency['eur'] = r.json()

source_currency = input("Enter currency source: ").lower()

exchanged = 0

while True:

    target_currency = input("Enter currency target or hit <Enter> to exit: ").lower()

    if target_currency == '' or source_currency == '':

        break

    else:

        amount = int(input("Enter amount to convert: "))

        print("Checking the cache...")

        if target_currency in cache_currency.keys():

            print("Oh! It is in the cache!")

            exchanged = amount / cache_currency[target_currency][source_currency]["rate"]

            print("Rate Date: ", cache_currency[target_currency][source_currency]['date'])

            print(f'You received {round(exchanged, 2)} {target_currency.upper()}.')

        else:

            print("Sorry, but it is not in the cache!")

            address = f"http://www.floatrates.com/daily/{target_currency}.json"

            req = requests.get(address, headers=user_agent)

            cache_currency[target_currency] = req.json()

            exchanged = amount / cache_currency[target_currency][source_currency]["rate"]

            print("Rate Date: ", cache_currency[target_currency][source_currency]['date'])

            print(f'You received {round(exchanged, 2)} {target_currency.upper()}.')

# for key, value in cache_currency.items():
#
#     print(key, value)
