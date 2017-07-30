import sqlite3
import time
import datetime
import random

from notdb import *


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

def getData():
    pass

def main():

    # For testing purposes only
    storeData('Jöchen Michäel Ding', '10a', 'Fach', 'Leistung', 1, 'Anmerkungen')

if __name__ == "__main__":
    main()
