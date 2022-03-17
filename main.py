import os
import pandas as pd


menu = pd.read_csv('menu.csv', header=1, encoding='UTF-8')
print(menu)
potrawy = []
jedzenie = menu.columns.tolist()
jedzenie_set = set(jedzenie)

def menu_creator():

    print("What?")
    key = input("Dish ")
    recipe = {key: []}

    while True:
        input_arg = input("Ingredient ")
        if input_arg != 'Koniec':
            recipe[key].append(input_arg)
            continue
        elif input_arg == "Koniec":
            print(recipe)
            break



def dodawanie():
    for arg in jedzenie:
        print()
    while True:
        nowe = input("Dodaj obiadek: ")
        potrawy.append(nowe)
        if nowe in jedzenie and nowe != "Koniec":
            print("{} dodano do listy obiadków".format(nowe))
            jedzenie_set.remove(nowe)
            print("W bazie pozostało:", *jedzenie_set, sep=", ")
            continue
        elif nowe== "Koniec":

            while '' in jedzenie_set:
                jedzenie_set.remove('')
            print("Twoja lista zakupów to: ", *jedzenie_set, sep='\n- ')
            break
        else:
            print("Nie ma takiego")
            continue


def inne():
    print("----------------\nChcesz dodać coś jeszcze?\nJeśli nie, ponownie wpisz Koniec")
    while True:
        dodatkowe = input("Dodaj: ")
        if dodatkowe== "Koniec":
            jedzenie_set=set(jedzenie)
            print("Twoja lista zakupów to: ", *jedzenie_set, sep='\n- ')
            break
        else:
            jedzenie.append(dodatkowe)
            continue

def usuwanie():
    print("----------------\nMasz już coś? Wpisz aby usunąć, lub wpisz Koniec, aby przejść do podsumowania!")
    while True:
        usuwane = input("Usuń: ")
        if usuwane == "Koniec":
            jedzenie_set = set(jedzenie)
            print("Twoja lista zakupów to: ", *jedzenie_set, sep='\n- ')
            break
        for y in jedzenie:
            if usuwane in jedzenie:
                jedzenie.remove(usuwane)
                jedzenie_set = set(jedzenie)
                print("Usunięto! Twoja lista zakupów to: ", *jedzenie_set, sep='\n- ',)
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
            jedzenie_set = set(jedzenie)
            print("Gratulacje! Twoja lista zakupów to: \n-------------", *jedzenie_set, sep='\n- ',)
            print("-------------")
            adres_mail = input("Podaj maila, na który wysłać listę: ")
            break
        else:
            print("Błąd")
            continue

    with open('lista.txt', 'w', encoding="utf8") as filehandle:
        for jedzenia in jedzenie:
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

    os.remove("lista.txt")



print("------------- \nWitaj w generatorze listy zakupów!\n-------------\nBaza danych zawiera:")
print(*jedzenie, sep=', ')

menu_creator()
dodawanie()
inne()
usuwanie()
podsumowanie()
