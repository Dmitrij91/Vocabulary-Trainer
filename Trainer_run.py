from Tkinter_gui import Eingabe
from Tkinter_gui import AbfrageModus
from tkinter import*
import tkinter as tk
class Vokabeltrainer():
    def __init__(self):
        self.fenster = Tk()
        self.background_image  = PhotoImage(file = "Brain.gif")
        self.Frame1 = Frame(self.fenster, width = 1000, height = 800, bd = 100,relief = "sunken" ) # bd (borderwidth)
        self.Frame1.grid(column = 0, row = 0, padx = 10, pady = 10)
        self.background_label = Label(self.Frame1, image=self.background_image, width = 1000, height = 200)
        self.background_label.place(x=0, y=0)
        self.Bild1 = Label(self.Frame1, text = "Willkommen beim Vokabeltrainer!!!", font = "title_font")
        self.Bild1.grid(column = 0, row = 0)
        self.Knopf = Button(self.Frame1, text = "Verlassen", command = self.Verlassen)
        self.Knopf.grid(column = 0, row = 1, pady = 10)
        self.Knopf1 = Button(self.Frame1, text = "Erschaffe Units", command = self.Erschaffe_Units)
        self.Knopf1.grid(column = 1, row = 1, pady = 10)
        self.fenster.mainloop()
    def Verlassen(self):
        pass
    def Erschaffe_Units(self):
        Eingabe()
    def ZeigeRahmen(self,Name):
        Rahmem = self.Name
            
    def Startfenster(self):
        self.Bild = Label(self, text="Willkommen beim Vokabeltrainer!!!")
        Knopf1 = tk.Button(self, text="Erschaffe Units",
                            command=lambda: controller.self.ZeigeRahmen("Unitauswahl"))
        Knopf1.pack()
        
class Startfenster(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Willkommen beim Vokabeltrainer!!!")
        label.pack(side="top", fill="x", pady=10)

        Knopf1 = tk.Button(self, text="Erschaffe Units",
                            command=lambda: controller.ZeigeRahmen("Unitauswahl"))
        Knopf1.pack()
class Unitauswahl(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gebe die Anzahl der Units ein")
        label.pack(side="top", fill="x", pady=10)
        self.eingabe = Entry(self)
        self.eingabe.pack()
        Knopf1 =tk.Button(self, text = "Eingabe", command = self.Vokabeleingabe)
        Knopf1.pack()
        Knopf = tk.Button(self, text = "Zum Startmenü", command= lambda :controller.ZeigeRahmen("Startfenster"))
        # mit Holfe von Lambda Operator lassen sich Werte an die Knöpfe zuweisen.
        Knopf.pack()
    def ZeigeRahmen(self, page_name):
        frame = self.Rahmen[page_name]
        frame.tkraise()
    def Vokabeleingabe(self):
        self.Anzahl = self.eingabe.get()
        self.eingabe.delete(0,20)
v = Vokabeltrainer()
#        for k in range(self.Anzahl):
 #           l = Eingabe()
 #           self.Units.append(l.Vokabular)
#            print(l.Vokabular)
