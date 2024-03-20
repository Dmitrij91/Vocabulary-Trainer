from tkinter import*
import random
import ast
import time
class Memory:
    def __init__(self,Liste):
        self.fenster = Tk()
        self.fenster.title("Vokabel-Memory")
        self.gefunden = 0
        self.versuche = 0
        self.LeereListe = []
        self.Spielfeld = []
        self.Liste = Liste
        self.fixiert = []
        self.geöffnet2 = []
        self.PaareFest = []
        self.Versuche = 0
        self.gelernt = 0
        self.Knopf = Button(self.fenster, text = "Mischen", command = self.Mischen, anchor = W)
        self.Knopf.grid()
#            self.Knopf = Button(text = "Mischen", command = self.Mischen)
#            self.c.create_Button(text = "mischen")
        for k in range(len(self.Liste)):
            for f in range(1):
                d = ast.literal_eval(Liste[k])
                l = list(d)
                self.PaareFest.append(l[0])
                self.PaareFest.append(d[l[0]])
        self.Paare = []
        for k in range(len(self.Liste)):
            for f in range(1):
                d = ast.literal_eval(Liste[k])
                l = list(d)
                self.Paare.append(l[0])
                self.Paare.append(d[l[0]])
        random.shuffle(self.Paare)
        for k in range(len(self.Liste)):
            for l in range(2):
                self.Button = Button(self.fenster)
                self.Button.grid(row = k+1,column = l+1)
                self.Button.bind("<ButtonRelease-1>", self.geklickt)
                self.Spielfeld.append(self.Button)
        for i in range(len(self.Spielfeld)):
            self.LeereListe.append(" ")
        self.now = 0
        self.Uhr = Label(self.fenster ,text ="Zeit:"+ str(self.now))
        self.Uhr.grid()
        while True :
            if len(self.fixiert) == len(self.PaareFest):
                break
            else:
                self.updateUhr()
                break
        self.ErschaffeSpielfeld()
        self.Knopf1 = Button(self.fenster, text = "Hilfe",command = self.Hilfe)
        self.Knopf1.grid()
        self.Knopf2 = Button(self.fenster, text = "Neustart", command = self.Neu)
        self.Knopf2.grid()
        print(self.PaareFest)
        print(self.Paare)
        self.Gefunden = Label(self.fenster,bg = "yellow", text = "Gefunden:"+str(self.gefunden))
        self.Gefunden.grid()
        self.Versuche = Label(self.fenster,bg = "blue", text = "Versuche:"+str(self.versuche))
        self.Versuche.grid()
        self.fenster.mainloop()
    def updateUhr(self):
        self.now += 1
        self.Uhr.configure(text = "Zeit:" +str(self.now))
        self.fenster.after(1000, self.updateUhr)
    def Mischen(self):#Fehler nicht die Paare mischen!
        random.shuffle(self.Paare)
        for (pos,item) in self.fixiert:
            b = self.Paare.index(item)
            self.Paare[pos], self.Paare[b] = self.Paare[b], self.Paare[pos]
        self.ErschaffeSpielfeld()
    def Hilfe(self):
        umgedreht = 0
        if umgedreht == 0:
            for key in self.PaareFest:
                if key not in self.LeereListe:
                    umgedreht += 1
                    a1 = self.Paare.index(key)
                    a = self.PaareFest.index(key)
                    b = self.Paare.index(self.PaareFest[a+1])
                    self.LeereListe[a1] = key
                    self.LeereListe[b] = self.Paare[b]
                    self.ErschaffeSpielfeld()
                    return umgedreht
    def Neu(self):
        self.fenster.destroy()
        k = Memory(self.Liste)
#        if event.widget == self.Knopf1:
#            k = self.LeereListe.index(" ")
#            self.Spielfeld[k].invoke()
#            a = self.PaareFest.index(self.Paare[k])
#            if a%2 == 0: # Tippe Deutsches Wort
#                Übersetzung = self.PaareFest[a+1]
#                b = self.Paare.index(Übersetzung)
#                self.Spielfeld[b].invoke()
#            else: #Tippe Englisches Wort
#                übersetzung = self.PaareFest[a-1]
#                b = self.Paare.index(übersetzung)
#                self.Spielfeld[b].invoke()
#        if len(self.geöffnet2) == 1:
#            a1 = self.Paare.index(self.geöffnet2[0])
#            a = self.PaareFest.index(self.Paare[a1])
#            if a%2 == 0: # Tippe Deutsches Wort
#                Übersetzung = self.PaareFest[a+1]
#                b = self.Paare.index(Übersetzung)
#                self.Spielfeld[b].configure(command = self.geklickt)
#                self.ErschaffeSpielfeld()
#            else: #Tippe Englisches Wort
#                übersetzung = self.PaareFest[a-1]
#                b = self.Paare.index(übersetzung)
#                self.Spielfeld[b].configure(command = self.geklickt)
#                self.ErschaffeSpielfeld()
    def geklickt(self,event):
        for i in range(len(self.Spielfeld)):
            if event.widget == self.Spielfeld[i]:
#                self.geöffnet2.append(self.Paare[i])
                self.Ausgabe(i)
    def ErschaffeSpielfeld(self):
        for i in range(len(self.Spielfeld)):
            self.Spielfeld[i].configure(text = self.LeereListe[i])
    def Ausgabe(self,i):
        if not self.geöffnet2:
            self.geöffnet2.append(self.Paare[i])
            self.LeereListe[i] = self.Paare[i]
            self.ErschaffeSpielfeld()
        elif len(self.geöffnet2) == 1:
            a1 = self.Paare.index(self.geöffnet2[0])
            a = self.PaareFest.index(self.Paare[a1])
            b = self.PaareFest.index(self.Paare[i])
            if a%2 == 0 and a != 0: #Deutsches Wort eungeben
#Bei geraden stehen die Schlüssel, bei ungeraden die Werte
                if self.PaareFest[a+1] == self.Paare[i]:
                    self.LeereListe[i] = self.Paare[i]
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()#Elemente fixieren
                    self.fixiert.append((a1,self.Paare[a1]))
                    self.fixiert.append((i,self.Paare[i]))
#                    self.Paare.remove(self.PaareFest[a])
#                    self.Paare.remove(self.PaareFest[a+1])
                else:
                    self.LeereListe[i] = " "
                    self.LeereListe[a1] = " " 
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()
            elif  a%2 != 0: #Englisches Wort eingeben
                if self.PaareFest[a-1] == self.PaareFest[b]:
                    self.LeereListe[i] = self.Paare[i]
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()
                    self.fixiert.append((a1,self.Paare[a1]))
                    self.fixiert.append((i,self.Paare[i]))
#                    self.Paare.remove(self.PaareFest[a])
#                    self.Paare.remove(self.PaareFest[a-1])
                else:
                    self.LeereListe[i] = " "
                    self.LeereListe[a1] = " " 
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()
                    
            else:
                if self.Paare[i] == self.PaareFest[1]:
                    self.LeereListe[i] = self.Paare[i] 
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()
                    self.fixiert.append((a1,self.Paare[a1]))
                    self.fixiert.append((i,self.Paare[i]))
#                    self.Paare.remove(self.PaareFest[0])
#                    self.Paare.remove(self.Paare[0])
                else:
                    self.LeereListe[i] = " "
                    self.LeereListe[a1] = " " 
                    self.geöffnet2 = []
                    self.ErschaffeSpielfeld()
        else:
            self.geöffnet2 = []
#            a = self.Paare.index(self.geöffnet[0])
#            b = self.Paare.index(self.geöffnet[1])
            self.LeereListe[i] = self.Paare[i]
            self.ErschaffeSpielfeld()
        print(self.LeereListe)
        print(self.Paare)