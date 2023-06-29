import tkinter as tk
from LingoLogica import Lingo
from LingoLeaderboard import Leaderboard

lingo = Lingo()
Leaderbord1 = Leaderboard()


window = tk.Tk()
window.title('Hello_World')
window.geometry('400x350')
window.configure(bg='pink')


label_out = tk.Label(window, text="LINGO",
    background="pink",
    padx=200,
    pady=70
)
label_out.pack()

label_naam = tk.Label(window, text="Naam:",
    background="pink",
)
label_naam.pack()

naam = tk.Entry(
    master=window, width=20,
    background="pink",
    foreground="pink"
)
naam.pack()

lingo_uitvoer = tk.Label(window, text="",
    background="pink"
)
lingo_uitvoer.pack()

label_leeftijd = tk.Label(window, text="Raad hier :")
label_leeftijd.pack()

entry = tk.Entry(
    master=window, width=60,
    background="purple",
    foreground="pink"
)
entry.pack()

btn_submit = tk.Button(master=window, text="Raad")
btn_submit.pack()

btn_clear = tk.Button(master=window, text="Overnieuw")
btn_clear.pack()

def handle_clear(event):
    entry.delete(0, 'end')


def handle_submit(event):
    try:
        staataan = 1
        invoer = (entry.get())
        score =10
        
        print(lingo.woord)
        uitvoer = lingo.invoercontrole(invoer)
        lingo_uitvoer["text"] = uitvoer

        while staataan == 1:
            print(score)
            if uitvoer != "Gewonnen":
                score -= 1
            if uitvoer == "Gewonnen":
                Leaderbord1.Add_score((naam.get()) , score)
                staataan = 0      
            staataan = 0
    except:
        label_out["text"] = "probeer opnieuw"
        entry.delete(0, 'end')

btn_submit.bind("<Button-1>", handle_submit)
btn_clear.bind("<Button-1>", handle_clear)

window.mainloop()