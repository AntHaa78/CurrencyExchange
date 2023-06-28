import os
import requests

def currency_list():
    while True:
        answer = input("Welcome to currency exchange. Do you wish to see the list of currencies available? y/n :")
        if answer != "y" and answer != "n":
            print("\n Please type y or n only")
            continue
        elif answer == "y":
            print('\n "EUR" "USD" "AUD" "JPY" "CAD" "GBP" "NZD" ')
            break
        else:
            break

def currency_exchange(dest,source):
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv('api_key')

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"to": dest, "from": source}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    converted_currency = response.json()
    return converted_currency


def final_result():
    dest = input("Select the destination quote: ")
    source = input("Select the source quote: ")
    quantity = input("Select the amount of currency to convert: ")
    converted_currency = currency_exchange(dest, source)
    quantity = int(quantity)
    converted_currency = float(converted_currency)
    final_result = converted_currency * quantity
    print(f"{quantity} {source} is worth {final_result} {dest}!")
