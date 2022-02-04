jedzenie = []
potrawy = []



import csv
reader = csv.reader(open('menu.csv'))




def nowa_rzecz():
    a_file = open("menu.csv", "a")
    klucz = input("Klucz: ")
    warto = []
    while True:
        wart = input("Wartość: ")
        if wart != "Koniec":
            print("Dodano")
            warto.append(wart)
            continue
        if wart == "Koniec":
            print("Zakończono")
            break
    print(*warto, sep=", ")
    nowaa = {klucz: dict[warto]}

    writer = csv.writer(a_file)
    for key, value in nowaa.items():
        writer.writerow([key, value])

    a_file.close()

def nowa_rzecz1111():
    a_file = open("menu.csv", "a")

    dict = {"Makaron": "Ser"}

    with open('menu.csv', 'w') as f:
        for key in dict.keys():
            f.write("%s, %s\n" % (key, dict[key]))

    a_file.close()


def dodawanie():
    for key in jedzenie_dict:
        print()
    while True:
        nowe = input("Dodaj obiadek: ")
        potrawy.append(nowe)
        if nowe in jedzenie_dict and nowe != "Koniec":
            print("{} dodano do listy obiadków".format(nowe))
            jedzenie.extend(jedzenie_dict[nowe])
            del jedzenie_dict[nowe]
            print("W bazie pozostało:", *list(jedzenie_dict.keys()), sep=", ")
            jedzenie_set = set(jedzenie)
            continue
        elif nowe== "Koniec":
            jedzenie_set = set(jedzenie)
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
print(*list(jedzenie_dict.keys()), sep= ", ")


#nowa_rzecz()
dodawanie()
inne()
usuwanie()
podsumowanie()
