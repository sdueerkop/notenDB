import sqlite3
import time
import datetime
import random
import re

from config import *

# Die Abkürzung 'lot' in Variablennamen steht hier für 'List of Tuples'


def storeData(name, klasse, fach, leistung, note, anmerkungen):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    year = str(datetime.datetime.fromtimestamp(unix).strftime('%Y'))
    month = int(datetime.datetime.fromtimestamp(unix).strftime('%m'))
    halbjahr = "1" if (month < 2 and month >= 8) else "2"
    tableName = "{}_{}_{}".format(name.replace(' ', ''), year, halbjahr)
    c.execute('CREATE TABLE IF NOT EXISTS ' + tableName + ' (unix REAL, datestamp TEXT, Name TEXT, Klasse TEXT, Fach TEXT, Leistung TEXT, Note TEXT, Anmerkungen TEXT )') 
    c.execute("INSERT INTO " + tableName + " (unix, datestamp, Name, Klasse, Fach, Leistung, Note, Anmerkungen) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                             (unix, date, name, klasse, fach, leistung, note, anmerkungen)) 

    conn.commit()
    c.close()
    conn.close()


def getTableNames():

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    # Get all table names in the database
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    lot_tableNames = c.fetchall()
    c.close()
    conn.close()
    
    tableNames = []
    for t in lot_tableNames:
        tableNames.append(t[0])
    
    return sorted(tableNames)

def notenDurchschnittSchueler(tableName, fach):

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT Name FROM " + tableName )
    l_name = c.fetchall()
    name = l_name[0][0]
    c.execute("SELECT Note, Fach FROM " + tableName )
    notenUndFaecher = c.fetchall()
    c.close()
    conn.close()
    noten = []
    for n, f in notenUndFaecher:
        if f == fach and not n == 'unbenotet':
            noten.append(int(n))
    avg = sum(noten) / len(noten)
    halbjahr = re.search(r'_(\d)$', tableName).group(1)
#    halbjahr = m.group(1)
    jahr = re.search(r'\d\d\d\d', tableName).group(0)
    return avg, name, halbjahr, jahr

def notenDurchschnittKlasse(klasse, halbjahr, leistung):
    # return max, min, mean
    pass

def main():

    # For testing purposes only
#    storeData('Hanna Schmidt', '10a', 'Fach', 'Präsentation', 1, 'Anmerkungen')

    tables = getTableNames()
    print(tables)

if __name__ == "__main__":
    main()
