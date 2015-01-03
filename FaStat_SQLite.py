#!/usr/bin/env python

# Database...
import sqlite3

# koble til 
conn = sqlite3.connect('FaStat.Value.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Value') # obs. SLETTER databasen!!! Må bort

cur.execute('CREATE TABLE Value (ID INT PRIMARY KEY NOT NULL,ATC TEXT NOT NULL,ATC_NAME TEXT NOT NULL, Jan_2015 DATE, Des_2014 DATE)') # Lager databasen med disse kolonnene, burde holde med første gang!? Burde ATC være key, eller ikke så farlig?

# Sjekk om kolonnen finnes allerede, hvis ikke legg til!
try:
    cur.execute('ALTER TABLE Value ADD COLUMN test_2014')
except:
    pass




conn.commit() # Lagre endringer
conn.close() # Lukk database-koblingen

# En database for siste kjøring (36 mnd)
# En database løpende per år??
# En database per komplette år??

# Populate one table using another table:

#You can populate data into a table through select statement over 
#another table provided another table has a set of fields, which 
#are required to populate first table. Here is the syntax:
#
#INSERT INTO first_table_name [(column1, column2, ... columnN)] 
#   SELECT column1, column2, ...columnN 
#   FROM second_table_name
#   [WHERE condition];
#
# Dvs. som dette ish:
#INSERT INTO Value [(Des_2014)] # Ny måned
#   SELECT Des_2014 # Ny måned
#   FROM Oppdatering_FaStat # Velge rett kolonne her og?
#   [WHERE condition]; # Value.ATC = Oppdatering_FaStat.ATC
