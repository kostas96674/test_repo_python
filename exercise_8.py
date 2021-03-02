"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Instructions to run program:
    Put the input file in the same directory as the python file.
    Run the program normally and give only the file name as the input.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import json

import requests


def find_crypto_wealth(coins):
    my_api_key = '1991344a6aa9fd3ae02af794d16ee9635629e64b4a78806e20fbfb6fc9952b44' #api key ncecessary to make http requests
    coins_string = ''

    for key in coins.keys(): #make a string containing all the user coins seperated with a coma so that it can be used correctly from the api
        coins_string += key + ","

    crypto_request = requests.get(
        f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={coins_string}&tsyms=EUR&api_key={my_api_key}') # make a GET request using the correct request structure of transforming mulriple coins to euro
    crypto_prices = json.loads(crypto_request.text) # make the string a python dictionary

    print('\nThe user has the following amount of EUR in each coin:\n')
    for coin, coin_amount in coins.items():
        coin_price = crypto_prices.get(coin).get('EUR') # the crypto_prices dict contains dicts for each different crypto and we get the euro value for each crypto
        user_coin_wealth = coin_price * coin_amount # the actual money of the user is the price of the coin multiplied by the amount of coins the possess.
        print(f"{coin}: {user_coin_wealth} EUR.")


if __name__ == '__main__':
    filename = str(input("Please insert the name of the file you want to analyze: "))
    f = open(f"{filename}.txt", "r")
    user_coins = json.loads(f.read())
    find_crypto_wealth(user_coins)
    f.close()
