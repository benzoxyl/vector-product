# TODO: - Abfangen von leeren Eingaben (Typ None)
#       - Programmfenster benennen
#       - Aufbereiten der Grafik yeet
#           - Vektoren nebeneinander, nicht untereinander yeet
#           - Begrenzung Länge der Labels, yeetssssssss
#           - Einfügen von Vektorklammern, = und x Zeichen yeet
#       - Aufräumen des Codes/Feedback von anderen

from tkinter import Tk, Label, Entry, Button, mainloop, messagebox
from PIL import Image, ImageTk

def formatFloat(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num

def vectorProduct():
    a = [None] * 3
    b = [None] * 3
    n = [None] * 3
    # Abfrage der a1-3 und b1-3 Werte
    for i in range(0,3):
        t = eval("e" + str(i) + ".get()")
        try:
            a[i] = formatFloat(float(t))
        except:
            messagebox.showerror("Error", "Please enter a number for a" + str(i) + " .")
            return
        
    for i in range(3,6):
        t = "e" + str(i) + ".get()"
        try:
            b[i-3] = formatFloat(float(eval(t)))
        except:
            messagebox.showerror("Error", "Please enter a number for b" + str(i-3) + " .")
            return

    # Berechnung des Kreuzproduktes
    n[0] = a[1]*b[2] - a[2]*b[1]
    n[1] = a[2]*b[0] - a[0]*b[2]
    n[2] = a[0]*b[1] - a[1]*b[0]

    # Ausgabe des Kreuzproduktes
    for i in range(1,4):
        exec("label" + str(i) + "['text']" + " = n[i-1]")

# Erstellen eines Tkinter Parent
root = Tk()
root.title("Kreuzprodukt")

# Definieren der Klammern
klauf = Image.open("/home/daniel/Downloads/klauf.png")
klauf = ImageTk.PhotoImage(klauf)

klzu = Image.open("/home/daniel/Downloads/klzu.png")
klzu = ImageTk.PhotoImage(klzu)

# Platzieren der Klammern
for i in range(0, 9, 4):
    Label(root, image=klauf).grid(column=i, row=0, rowspan=3)
    Label(root, image=klzu).grid(column=i+2, row=0, rowspan=3)
    
Label(root, text="x").grid(column=3, row=1)
Label(root, text="=").grid(column=7, row=1)

# Erstellung und Sortieren der Eingabefelder e0-2
for i in range(0,3):
    exec("e" + str(i) + " = Entry(root, width=3)")
    exec("e" + str(i) + ".grid(row=" + str(i) + ", column=1)")

# Erstellung und Sortieren der Eingabefelder e3-5
for i in range(3,6):
    exec("e" + str(i) + " = Entry(root, width=3)")
    exec("e" + str(i) + ".grid(row=" + str(i-3) + ", column=5)")

# Knopf für die Berechnung des Vektorproduktes
Button(root, text="Calculate!", command=vectorProduct).grid(row=1, column=11)

for i in range(1,4):
    # Erstellung Labels für n1-3 ERGEBNISSE
    exec("label" + str(i) + " = Label(root, width=3)")
    exec("label" + str(i) + ".grid(row=i-1, column=9)")

# Loop der das Windows zeichner
mainloop()
