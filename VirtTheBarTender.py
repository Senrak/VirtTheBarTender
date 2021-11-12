#!/usr/bin/python3
#Author: Brayden Karnes
#Description: Virtual bar tender using The Cocktial DB API

import requests
import json

url = "https://the-cocktail-db.p.rapidapi.com/"

#HEADERS
headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "<INSERT API KEY HERE>"
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

def testing_menu():
    print()
    print('1. random_ten')
    print('2. drink_search')
    choice = input('Enter choice: ')
    
    return choice

def random_ten():

    #VARIABLES
    ingredients = []
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
            ingredients.append(response['drinks'][x][var])
            print(response['drinks'][x][var])
        #print(*ingredients, sep = ", ")
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

main()
