import sqlite3
from datetime import datetime
import csv

tdate = datetime.today().strftime("%d-%m-%Y")

con = sqlite3.connect('watchlist.db', check_same_thread=False)


def createtable():
    cur = con.cursor()
    cur.execute('''CREATE TABLE animes 
    (id INTEGER PRIMARY KEY, name text NOT NULL UNIQUE, ep int, wstate BOOLEAN NOT NULL CHECK (wstate IN (0, 1)), date text, online BOOLEAN NOT NULL CHECK (online IN (0, 1)));''')
    con.commit()


def addrow(name):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO animes (date, name, ep, wstate, online) VALUES (?, ?, 0, 0, 1);", (tdate, name))
    con.commit()


def updaterow(operation, data, name):
    cur = con.cursor()
    if operation == 'ep':
        cur.execute("UPDATE animes SET ep=:var WHERE name=:aniname;", {'var': data, 'aniname': name})
    else:
        cur.execute("UPDATE animes SET wstate=:var WHERE name=:aniname;", {'var': data, 'aniname': name})
    con.commit()


def returnrows():
    cur = con.cursor()
    data = cur.execute("SELECT * FROM animes;")
    return data


def exportcsv():
    with open('exportlist.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'name', 'ep', 'wstate', 'online'])
        writer.writerows(returnrows())


def importcsv():
    cur = con.cursor()
    with open('exportlist.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        to_db = [(i['id'], i['date'], i['name'], i['ep'], i['wstate'], i['online']) for i in reader]
        cur.execute("DROP table IF EXISTS animes")
        cur.execute('''CREATE TABLE animes 
        (id INTEGER PRIMARY KEY, date text, name text NOT NULL UNIQUE, ep int, wstate BOOLEAN NOT NULL CHECK (wstate IN (0, 1)), online BOOLEAN NOT NULL CHECK (online IN (0, 1)));''')
        for row in to_db:
            print(row)
            cur.execute(
            "INSERT INTO animes (id, date, name, ep, wstate, online) VALUES (?, ?, ?, ?, ?, ?);", row)
        con.commit()

# createtable()
# addrow('fire force')
# con.execute("DELETE FROM animes WHERE name='fire force'")
# updaterow('ep',7,"No Gun's Life S1")
# updaterow('state',0)
# exportcsv()
# importcsv()
# print([row for row in returnrows()])