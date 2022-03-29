import os
import pandas as pd
from os.path import exists
import json



potrawy = []
skladniki = []
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


    f = open('json_data.json', 'r')
    recipe = json.load(f)

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
                    recipe = recipe.setdefault(key2,[]).append(values2)
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

    with open("json_data.json", "r+") as file:
        json.dump(recipe, file)





def dodawanie():


    while True:
        nowe = input("Dodaj obiadek: ")
        potrawy.append(nowe)
        if nowe in jedzenie and nowe != "Koniec":
            print("{} dodano do listy obiadków".format(nowe))
            ing = menu[nowe].tolist()
            skladniki.extend(ing)
            skladniki_set = set(skladniki)

            jedzenie_set.remove(nowe)
            print("W bazie pozostało:", *jedzenie_set, sep=", ")
            continue
        elif nowe== "Koniec":

            while '' in jedzenie_set:
                jedzenie_set.remove('')
            print("Twoja lista zakupów to: ", *skladniki_set, sep='\n- ')

            break
        else:
            print("Nie ma takiego")
            continue


def inne():
    print("----------------\nChcesz dodać coś jeszcze?\nJeśli nie, ponownie wpisz Koniec")
    while True:
        dodatkowe = input("Dodaj: ")
        if dodatkowe== "Koniec":
            skladniki_set = set(skladniki)
            print("Twoja lista zakupów to: ", *skladniki_set, sep='\n- ')
            break
        else:
            skladniki.append(dodatkowe)
            continue

def usuwanie():
    print("----------------\nMasz już coś? Wpisz aby usunąć, lub wpisz Koniec, aby przejść do podsumowania!")
    while True:
        usuwane = input("Usuń: ")
        if usuwane == "Koniec":
            skladniki_set = set(skladniki)
            print("Twoja lista zakupów to: ", *skladniki_set, sep='\n- ')
            break
        for y in skladniki:
            if usuwane in skladniki:
                skladniki.remove(usuwane)
                skladniki_set = set(skladniki)
                print("Usunięto! Twoja lista zakupów to: ", *skladniki_set, sep='\n- ',)
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
            skladniki_set = set(skladniki)
            print("Gratulacje! Twoja lista zakupów to: \n-------------", *skladniki_set, sep='\n- ',)
            print("-------------")
            adres_mail = input("Podaj maila, na który wysłać listę: ")
            break
        else:
            print("Błąd")
            continue

    with open('lista.txt', 'w', encoding="utf8") as filehandle:
        for jedzenia in skladniki:
            filehandle.write('%s\n' % jedzenia)

    import email, smtplib, ssl, os

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Lista zakupów"
    body = "This is an email with attachment sent from Python"
    sender_email = "obiad.burner@gmail.com"
    receiver_email = adres_mail
    password = "Tomek1994"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    filename = 'lista.txt'

    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

#os.remove("lista.txt")

################################################################
#START#
################################################################
file_exists = exists('json_data.json')
if file_exists:
    menu_creator()

else:
    menu_scratch()


jedzenie = menu.keys.tolist()
jedzenie_set = set(jedzenie)
print("------------- \nWitaj w generatorze listy zakupów!\n-------------\nBaza danych zawiera:")
print(*jedzenie, sep=', ')







dodawanie()
inne()
usuwanie()
podsumowanie()
