import sqlite3
import os
class Lingo:

    # constructor
    def __init__(self):
        self.woord = self.set_woord()
        print(self.woord)
        print("woord = " + self.woord)

    def set_woord(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "lingo.sqlite3")
        connection = sqlite3.connect(db_path)
        #connection = sqlite3.connect('lingo.sqlite3')
        Winwoord = ""
        cursor = connection.execute('SELECT * FROM zesletters ORDER BY RANDOM() LIMIT 1;')
        for row in cursor:
            Winwoord = row[0]
        connection.close()
        print(Winwoord)
        return Winwoord

    def invoercontrole(self, invoer):
        invoer = invoer.lower()
        print(invoer)
        uitvoer = []
        Winwoord = self.woord
        if Winwoord != "":
            if invoer == Winwoord:
                print("Gewonnen!")
                return("Gewonnen")
            if (len(invoer)!= 6):
                return("Het woord moet uit 6 letters bestaan")

            for i in range(0,6):
                print(i) 
                #print("vergelijk: " + invoer[i] + " met " + Winwoord[i])
                if invoer[i] == Winwoord[i]:
                    print("goed: " + str(i))
                    uitvoer.append(invoer[i].upper())
                elif invoer[i] in Winwoord:
                    uitvoer.append(invoer[i])
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                elif invoer[i] not in Winwoord:
                    uitvoer.append("-")
        else:
            print("fout oof")

        print(uitvoer)
        return(uitvoer)

    