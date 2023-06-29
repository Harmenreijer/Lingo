from datetime import date
import sqlite3
import os
class Leaderboard:
    def __init__(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS highscores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, score INTEGER NOT NULL); """)
        connection.close()

    def Add_score(self, name , score):
        print("allo")
        #import datetime
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "lingo.sqlite3")
        connection = sqlite3.connect(db_path)
        #connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()
        #cursor.execute("""CREATE TABLE IF NOT EXISTS highscores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, score INTEGER NOT NULL); """)
       

        #cursor = self.db.connection.cursor()
        nu = date.now()
        query = "INSERT INTO highscores (name, date, score) VALUES (?,?,?)"
        cursor.execute(query,(name, score))
        #self.db.connection.commit() 
        connection.commit()
        connection.close()

