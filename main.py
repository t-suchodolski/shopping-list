import os
import pandas as pd
from os.path import exists



potrawy = []
skladniki = []
skladniki_set = set(skladniki)


def menu_scratch():
    output1 = pd.DataFrame()
    while True:
        ans1 = input("Add recipe? Y/N ")
        if ans1 == 'Y':
            key1 = input("What is it? ")
            values1 = []
            recipe1 = {key1: values1}
            while True:
                values1 = input("Ingredient: ")

                if values1 != "Koniec":
                    recipe1[key1].append(values1)
                    df1 = pd.DataFrame.from_dict(recipe1)
                    print(df1)
                    continue
                else:
                    break

            output1 = pd.concat([output1, df1], axis=1, ignore_index=False)
            continue
        elif ans1 == 'N':
            break
        else:
            print('Error, try again')
            continue


    new_col_menu1 = pd.DataFrame(output1)
    new_col_menu1.to_csv('menu.csv', index=False)

def menu_creator():
    output = pd.DataFrame()
    while True:
        ans = input("Add recipe? Y/N ")
        if ans == 'Y':
            key = input("What is it? ")
            values = []
            recipe = {key: values}
            while True:
                values = input("Ingredient: ")
                if values != "Koniec":
                    recipe[key].append(values)
                    df = pd.DataFrame.from_dict(recipe)
                    continue
                else:
                    break

            output = pd.concat([output, df], axis=1, ignore_index=False)
            continue
        elif ans == 'N':
            break
        else:
            print('Error, try again')
            continue


    new_col_menu = pd.DataFrame(output)
    creator = pd.concat([menu, new_col_menu],axis=1)
    creator.to_csv('menu.csv', index=False)



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
file_exists = exists('menu.csv')
if file_exists:
    menu = pd.read_csv('menu.csv', header=0, encoding='UTF-8')
    menu_creator()
else:
    menu_scratch()
    menu = pd.read_csv('menu.csv', header=0, encoding='UTF-8')


jedzenie = menu.columns.tolist()
jedzenie_set = set(jedzenie)
print("------------- \nWitaj w generatorze listy zakupów!\n-------------\nBaza danych zawiera:")
print(*jedzenie, sep=', ')







dodawanie()
inne()
usuwanie()
podsumowanie()
