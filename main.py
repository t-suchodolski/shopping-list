import os
from datetime import date
from os.path import exists
import json


selection = []
ingredient = []
shopping_list = []
ingredient_set = set(ingredient)

def menu_scratch():

    while True:
        ans1 = input("Add recipe? Y/N ").capitalize()
        if ans1 == 'Y':
            key2 = input("What is it? ").capitalize()
            values2 = []
            recipe = {key2: values2}

            while True:
                values2 = input("Add ingredient. Type Done to save: ").capitalize()
                if values2 != "Done":
                    recipe.setdefault(key2,[]).append(values2)
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
        ans2 = input("Add recipe? Y/N ").capitalize()
        if ans2 == 'Y':
            key2 = input("What is it? ").capitalize()
            values2 = []
            recipe[key2] = values2

            while True:
                values2 = input("Add ingredient. Type Done to save: ").capitalize()
                if values2 != "Done":
                    recipe.setdefault(key2,[]).append(values2)
                    continue
                else:
                    break
            continue
        elif ans2 == 'N':
            break
        else:
            print('Error, try again')
            continue


    with open("menu.json", "a+") as file:
        json.dump(recipe, file)

def menu_creator():


    f = open('menu.json', 'r')
    recipe = json.load(f)
    f.close()
    os.remove('menu.json')
    while True:
        ans2 = input("Add recipe? Y/N ").capitalize()
        if ans2 == 'Y':
            key1 = input("What is it? ").capitalize()
            values1 = []
            recipe1 = {key1: values1}

            while True:
                values1 = input("Add ingredient, type Done to save: ").capitalize()
                if values1 != "Done":
                    recipe1[key1].append(values1)
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

def add():

    while True:
        new = input("Add recipe or type Done to finish: ").capitalize()
        selection.append(new)
        if new in rec_key and new != "Done":
            print("{} added to your recipe list".format(new))
            ingredient = recipe.get(new)
            shopping_list.extend(ingredient)
            rec_key_set.remove(new)
            print("Recipes left: ", *rec_key_set, sep=", ")
            continue
        elif new== "Done":

            while '' in rec_key_set:
                rec_key_set.remove('')

            shopping_list_set = set(shopping_list)
            print("Your shopping list: ", *shopping_list_set, sep='\n- ')

            break
        else:
            print("Object unavailable")
            continue


def other():
    print("----------------\nWould you like to add anything more?\nIf not, type Done again")
    while True:
        dodatkowe = input("Add: ").capitalize()
        if dodatkowe== "Done":
            shopping_list_set = set(shopping_list)
            print("Your shopping list: ", *shopping_list_set, sep='\n- ')
            break
        else:
            shopping_list.append(dodatkowe)
            continue

def delete():
    print("----------------\nGot something already? Type it to delete, or type Done to proceed to summary!")
    while True:
        usuwane = input("Delete: ").capitalize()
        if usuwane == "Done":
            shopping_list_set = set(shopping_list)
            print("Your shopping list: ", *shopping_list_set, sep='\n- ')
            break
        for y in shopping_list:
            if usuwane in shopping_list:
                shopping_list.remove(usuwane)
                shopping_list_set = set(shopping_list)
                print("Deleted! Your shopping list: ", *shopping_list_set, sep='\n- ',)
                print("----------------")
                break
            else:
                print("No such object!")
                break
        continue

def summary():
    while True:
        fin = input("-----------\nAlmost done! Type Recipe, Add, or Delete, To edit your list\nType Done to receive the list ").capitalize()
        if fin== "Recipe":
            add()
            continue
        elif fin== "Add":
            other()
            continue
        elif fin== "Delete":
            delete()
            continue
        elif fin== "Done":
            shopping_list_set = set(shopping_list)
            print("Congrats! Your shopping list: \n-------------", *shopping_list_set, sep='\n- ',)
            print("-------------")
            break
        else:
            print("Błąd")
            continue

    today = str(date.today())

    with open('shopping_list ' + today + '.txt', 'w', encoding="utf8") as filehandle:
        for jedzenia in shopping_list:
            filehandle.write('%s\n' % jedzenia)



################################################################
#START#
################################################################

boot = input('Open recipe creator? Y for yes, ENTER for skip: ').capitalize()
if boot == 'Y':
    file_exists = exists('menu.json')
    if file_exists:
        menu_creator()

    else:
        menu_scratch()

f = open('menu.json', 'r')
recipe = json.load(f)
rec_key = []
for key in recipe:
    rec_key.append(key)
rec_key_set = set(rec_key)
print("------------- \nWelcome to shopping list generator!!\n-------------\nYour database consists:")
print(*rec_key, sep=', ')

add()
other()
delete()
summary()
