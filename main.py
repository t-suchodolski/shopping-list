import os
from datetime import date
from os.path import exists
import json

potrawy = []
skladniki = []
lista = []
skladniki_set = set(skladniki)

def menu_scratch():

    while True:
        ans1 = input("Add recipe? Y/N ")
        if ans1 == 'Y':
            key2 = input("What is it? ")
            values2 = []
            recipe = {key2: values2}

            while True:
                values2 = input("Ingredient: ")
                if values2 != "Koniec":
                    #recipe[key1].append(values1)
                    recipe.setdefault(key2,[]).append(values2)
                    print(recipe)
                    continue
                else:
                    break
            break
        elif ans1 == 'N':
            break
        else:
            print('Error, try again')
            continue

    while True:
        ans2 = input("Add recipe? Y/N ")
        if ans2 == 'Y':
            key2 = input("What is it? ")
            values2 = []
            #recipe = {key1: values1}
            recipe[key2] = values2

            while True:
                values2 = input("Ingredient: ")
                if values2 != "Koniec":
                    #recipe[key1].append(values1)
                    recipe.setdefault(key2,[]).append(values2)
                    print(recipe)
                    continue
                else:
                    break
            continue
        elif ans2 == 'N':
            break
        else:
            print('Error, try again')
            continue

    print(recipe)
    with open("menu.json", "a+") as file:
        json.dump(recipe, file)

def menu_creator():


    f = open('menu.json', 'r')
    recipe = json.load(f)
    print(recipe)
    f.close()
    os.remove('menu.json')
    while True:
        ans2 = input("Add recipe? Y/N ")
        if ans2 == 'Y':
            key1 = input("What is it? ")
            values1 = []
            recipe1 = {key1: values1}
            #recipe[key2] = values2

            while True:
                values1 = input("Ingredient: ")
                if values1 != "Koniec":
                    recipe1[key1].append(values1)
                    #recipe = recipe.setdefault(key2,[]).append(values2)

                    continue
                else:
                    break
            continue
        elif ans2 == 'N':
            break
        else:
            print('Error, try again')
            continue


    recipe.update(recipe1)
    with open("menu.json", "a+") as file:
        json.dump(recipe, file)

def dodawanie():

    while True:
        nowe = input("Dodaj obiadek: ")
        potrawy.append(nowe)
        if nowe in jedzenie and nowe != "Koniec":
            print("{} dodano do listy obiadków".format(nowe))
            skladniki = recipe.get(nowe)
            lista.extend(skladniki)
            jedzenie_set.remove(nowe)
            print("W bazie pozostało:", *jedzenie_set, sep=", ")
            continue
        elif nowe== "Koniec":

            while '' in jedzenie_set:
                jedzenie_set.remove('')

            lista_set = set(lista)
            print("Twoja lista zakupów to: ", *lista_set, sep='\n- ')

            break
        else:
            print("Nie ma takiego")
            continue


def inne():
    print("----------------\nChcesz dodać coś jeszcze?\nJeśli nie, ponownie wpisz Koniec")
    while True:
        dodatkowe = input("Dodaj: ")
        if dodatkowe== "Koniec":
            lista_set = set(lista)
            print("Twoja lista zakupów to: ", *lista_set, sep='\n- ')
            break
        else:
            lista.append(dodatkowe)
            continue

def usuwanie():
    print("----------------\nMasz już coś? Wpisz aby usunąć, lub wpisz Koniec, aby przejść do podsumowania!")
    while True:
        usuwane = input("Usuń: ")
        if usuwane == "Koniec":
            lista_set = set(lista)
            print("Twoja lista zakupów to: ", *lista_set, sep='\n- ')
            break
        for y in lista:
            if usuwane in lista:
                lista.remove(usuwane)
                lista_set = set(lista)
                print("Usunięto! Twoja lista zakupów to: ", *lista_set, sep='\n- ',)
                print("----------------")
                break
            else:
                print("Nie ma tego na liście!")
                break
        continue

def podsumowanie():
    while True:
        fin = input("-----------\nPrawie koniec! Wpisz Obiad, Dodaj, lub Usuń, aby edytować listę\nWpisz Koniec, aby otrzymać maila z listą ")
        if fin== "Obiad":
            dodawanie()
            continue
        elif fin== "Dodaj":
            inne()
            continue
        elif fin== "Usuń":
            usuwanie()
            continue
        elif fin== "Koniec":
            lista_set = set(lista)
            print("Gratulacje! Twoja lista zakupów to: \n-------------", *lista_set, sep='\n- ',)
            print("-------------")
            break
        else:
            print("Błąd")
            continue

    today = str(date.today())

    with open('lista ' + today + '.txt', 'w', encoding="utf8") as filehandle:
        for jedzenia in lista:
            filehandle.write('%s\n' % jedzenia)



################################################################
#START#
################################################################

boot = input('Open recipe creator? Y for yes, ENTER for skip: ')
if boot == 'Y':
    file_exists = exists('menu.json')
    if file_exists:
        menu_creator()

    else:
        menu_scratch()

f = open('menu.json', 'r')
recipe = json.load(f)
jedzenie = []
for key in recipe:
    jedzenie.append(key)
jedzenie_set = set(jedzenie)
print("------------- \nWitaj w generatorze listy zakupów!\n-------------\nBaza danych zawiera:")
print(*jedzenie, sep=', ')

dodawanie()
inne()
usuwanie()
podsumowanie()
