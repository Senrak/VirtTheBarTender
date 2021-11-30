#!/usr/bin/python3
#Author: Brayden Karnes
#Description: Virtual bar tender using The Cocktial DB API

import requests
import json
from PIL import Image
import urllib.request
import tkinter as tk

url = "https://the-cocktail-db.p.rapidapi.com/"

#HEADERS
headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    
    'x-rapidapi-key': "<REPLACE WITH YOUR KEY>"
    }

#URL APPENDERS
url_filter = "filter.php"
url_search = "search.php"
url_multirandom = "randomselection.php"     #10 random
url_random = "random.php"
url_lookup = "lookup.php"
url_latest = "latest.php"
url_popular = "popular.php"
url_list = "list.php"

#URL APPEND OPTIONS
#querystring options:
#    LIST:
#       c: categories           {"c":"list"}
#       g: glasses              {"g":"list"}
#       i: ingredients          {"i":"list"}
#       a: alcoholic filters    {"a":"list"}
#    FILTER:
#       a: alocholic    {"a":"Alcoholic"}
#       c: category     {"c":"Cocktail"}  {"c":"Cocktail_glass"}
#       i: ingredients  {"i":"Dry_Vermouth, Gin, Anis"}
#    SEARCH:
#       i: ingredient   {"i":"vodka"}
#       s: cocktail     {"s":"Old Fashioned"}       

def main():
    choice = testing_menu()
    if choice == str(1):
        random_ten()
    elif choice == str(2):
        drink_search()
    elif choice == str(3):
        popular()
    elif choice == str(4):
        non_alcoholic()
    elif choice == str(5):
        search_ingredient()
    elif choice == str(6):
        testing_1()

def search_ingredient():
    url_appended = url + url_filter
    ingredients = input('Enter ingredients (seperated by commas): ')
    querystring = {"i":ingredients}

    response = requests.request("GET", url_appended, headers=headers, params=querystring).json()

    drink_num = len(response['drinks'])

    print('')
    for x in range(drink_num):
        print(f'{response["drinks"][x]["strDrink"] : <20}')

def testing_1():
    url_appended = url + url_random
    
    response = requests.request("GET", url_appended, headers=headers).json()

    urllib.request.urlretrieve(response['drinks'][0]['strDrinkThumb'],'img.png')

    img = Image.open("img.png")
    img.show()

    print(response)

def non_alcoholic():
    url_appended = url + url_filter
    querystring = {"a":"Non alcoholic"}

    response = requests.request("GET", url_appended, headers=headers, params=querystring).json()

    drink_num = len(response['drinks'])
        
    print('')
    for x in range(drink_num):
        print(f'{response["drinks"][x]["strDrink"] : <20}')

def popular():
    url_appended = url + url_popular

    response = requests.request("GET", url_appended, headers=headers).json()
    
    print('')
    print(f'{"Top 10 Drinks:" : <20}        {"Ingredients:" : <25}')

    for x in range(10):
        print(f'{response["drinks"][x]["strDrink"] : <20}  {response["drinks"][x]["strIngredient1"] : <25} {"& more" : <28}')

def testing_menu():
    print()
    print('1. random_ten')
    print('2. drink_search')
    print('3. popular')
    print('4. non_alcoholic')
    print('5. search_ingredients')
    print('6. random_drink')
    choice = input('Enter choice: ')
    
    return choice

def random_ten():
    url_appended = url + url_multirandom

    response = requests.request("GET", url_appended, headers=headers).json()
    
    for x in range(10):
        print('')
        print(response['drinks'][x]['strDrink'])
        print('Ingredients: ')
        for y in range(9):
            var = 'strIngredient' + str(y+1)
            if (response['drinks'][x][var]) == None:
                break
            print(response['drinks'][x][var])
        print('Instructions: ',response['drinks'][x]['strInstructions'])

def drink_search():
    url_appended = url + url_search

    drink_name = input("What drink would you like? ")
    querystring = {"s":drink_name}

    response = requests.request("GET", url_appended, headers=headers, params=querystring).json()
    
    print('')
    print('Ingredients: ')
    for x in range(9):
        ingredient_num = 'strIngredient' + str(x+1)
        if (response['drinks'][0][ingredient_num]) == None:
            break
        print(response['drinks'][0][ingredient_num])
    print('Instructions: ',response['drinks'][0]['strInstructions'])

    urllib.request.urlretrieve(response['drinks'][0]['strDrinkThumb'],'img.png')

    img = Image.open("img.png")
    img.show()

main()
