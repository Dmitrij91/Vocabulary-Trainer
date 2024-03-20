from Manage_Memory import Memory
from tkinter import*
import random 
import ast
from tkinter import messagebox
import time

class Eingabe:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Vokabel Memory")
        self.Vokabular = []
        self.Hilf = {}
        self.Ausgewählt = []
        self.vokabel = StringVar()
        self.Übersetzung = StringVar()
        Label(self.fenster,text = "Gebe die Wörter zum Üben ein", width = 30, height = 3).pack()
        Label(self.fenster,text = "Vokabel", width = 30, height = 3).pack()
        self.entry1 = Entry(self.fenster, textvariable=self.vokabel)
        self.entry1.pack()
        Label(self.fenster,text = "Übersetzung", width = 30, height = 3).pack()
        self.entry = Entry(self.fenster, textvariable=self.Übersetzung)
        self.entry.pack()
        self.Knopf1 = Button(self.fenster, text="Eingabe", command = self.Speichern).pack()
        self.Knopf2 = Button(self.fenster, text="Zum Spiel",command = self.WähleVokabeln)
        self.Knopf2.pack()
        self.fenster.mainloop()
    def Spiel1(self):
        k = AbfrageModus(self.d)
    def Spiel2(self):
        k = Memory(self.d)
    def Hilfe(self):
        for item in self.Vokabular:
            self.Hilf[str(item)] = int("0")
        return self.Hilf
    def BekommWerte(self):
        messagebox.showinfo("Spielinfo:",
                                     "Willkommen! Du hast folgende Spiele zum Vokabelüben:\n"
                                     "Vokabeltrainer: Üben im Abfragemodus\n"
                                     "Vokabel-Memory: Üben von Vokabeln durch finden richtiger Vokabelpaare.\n\n"
                                     "Viel Glück!!!")
        self.fenster1.destroy()
        self.fenster2 = Tk()
        self.d = []
        for key, value in self.Hilf.items():
            state = value.get()
            if state != 0:
                self.d.append(key)
                print(key)
                self.Hilf[key].set(0)
        self.Vokabeltrainer = Button(self.fenster2,text = "Zum Vokabeltrainer", command = self.Spiel1)
        self.Vokabeltrainer.pack()
        self.Vokabelmemory = Button(self.fenster2,text = "Zu Vokabel-Memory",command = self.Spiel2)
        self.Vokabelmemory.pack()
        self.fenster2.mainloop()
        print(self.d)
    def WähleVokabeln(self):
        messagebox.showinfo("Vokabeln erfolgreich gespeichert!")
        self.fenster.destroy()
        self.Hilf = self.Hilfe()
        self.fenster1 = Tk()
        Label(self.fenster1, text = "Wähle die Vokabeln die du lernen möchtest", width = 100, height = 6).pack()
        for key in self.Hilf:
            self.Hilf[key] = IntVar()
            aButton = Checkbutton(self.fenster1, text=key,variable = self.Hilf[key])
            aButton.pack()
        Knopf3 = Button(self.fenster1, text = "Los Gehts!",command = self.BekommWerte) 
        Knopf3.pack()
        self.fenster1.mainloop()
    def schließen(self):
        print(self.Hilf)
    def Speichern(self):
        d2 = {}
        d2[self.vokabel.get()] = self.Übersetzung.get()
        self.Vokabular.append(d2)
        self.entry.delete(0,20)
        self.entry1.delete(0,20)
class AbfrageModus:
    def __init__(self,Liste):
        self.Schlüssel_liste = random.shuffle(Liste)
#        self.fenster1.destroy()
        self.Abgefragt = []
        self.gelernt = 0
        self.Liste = Liste
        self.Schlüssel = self.NeuSchlüssel(self.Liste)
        self.Voc = self.NeuVoc(self.Liste)
        self.fenster2 = Tk()
        self.titel = Label(self.fenster2, text = "Gebe die richtige Übersetzung ein",width = 100, height = 6,fg = "blue")
        self.titel.pack()
        self.rahmen = Frame(self.fenster2,width= 30, height=20, relief = RIDGE, bd=5)
        self.Voc1 = StringVar()
        self.Voc1.set(self.Voc)
        self.wort1 = Label(self.rahmen,textvariable = self.Voc1, font=("Arial",14))
#        .replace("{","}"
        self.wort1.pack()
        self.wort2 = Label(self.rahmen,text = "Übersetzung", font=("Arial",14))
        self.wort2.pack()
        self.s = StringVar()
        self.eingabe = Entry(self.rahmen,textvariable = self.s, width=15)
        self.eingabe.pack()
        self.Knopf4 = Button(self.rahmen, text = "Prüfe!", command = self.Prüfe)
        self.Knopf4.pack()
        self.rahmen.pack()
        self.Zeige = Label(self.fenster2, 
                      width=10, bg='yellow',
                      text=str(self.gelernt)+' gelernt')
        self.Zeige.pack()
        self.Fenster = Label(self.fenster2, width=20)
        self.Fenster.pack()
        self.Knopf5 = Button(self.fenster2, text = "Nochmal", command = self.Nochmal)
        self.Knopf5.pack()
        self.Knopf6 = Button(self.fenster2,text = "Zurück zur Vokabelauswahl", command = self.zurück)
        self.Knopf6.pack()
        print(type(self.Schlüssel))
        print(self.Voc)
        self.fenster2.mainloop()
    def NeuSchlüssel(self,Liste):
        d = ast.literal_eval(Liste[0])
        k = list(d)[0]
        return d[k]
    def zurück(self):
        pass
    def Nochmal(self):
        self.Prüfe()
    def Prüfe(self):
        print("Funktioniere ich ?")
        if self.s.get() == self.Schlüssel:
            self.gelernt += 1
            self.Zeige.config(text = "Richtige Antwort")
            v = StringVar()
            v = str(self.gelernt)
            self.Zeige.config(text = "Gelernt"+v)
            self.Liste.pop(0)
            self.fenster2.after(1000, self.Schritt)
            print(self.Liste)
            
        else:
            self.Zeige.config(text = "Falsche Antwort")
            self.Liste.append(self.Liste[0])
            self.Liste.pop(0)
            print(self.Liste)
    def NeuVoc(self,Liste):
        try:
            d = ast.literal_eval(Liste[0])
            l = list(d)
            return l[0]
        except IndexError:
            self.Fenster.config(text='Alles gelernt!')
            self.eingabe.delete(0,15)
            
            
        
    def Schritt(self):
      self.Fenster.config(text='')
      self.eingabe.delete(0,15)
      self.Voc = self.NeuVoc(self.Liste)
      self.Schlüssel = self.NeuSchlüssel(self.Liste)
      self.Voc1.set(self.Voc)

#s = Eingabe()