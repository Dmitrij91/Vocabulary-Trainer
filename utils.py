import random

class Hauptprogram():
    def __init__(self):
        self.Anzahl = self.Anzahl()
    def Anzahl(self):
        r = input("Geben Sie die Anzahl der UNits an:\n")
        return r
    def Karteikarten(self):
       d={}
       englisch=input("Englisches Wort \n")
       while englisch:
          deutsch=input("Deutsche Übersetzung \n")
          d[englisch]=deutsch
          englisch=input("Englisches Wort \n")
       return d
    def Units(self):
        for i in range(int(self.Anzahl)):
            k = "Unit"+str(i+1)
            r = open(k+"txt","w")
            print("Gebe das Vokabular für"+k)
            Vokabeln = self.Karteikarten()
            r.write(str(Vokabeln))
    def ErschaffeDict(self,Datei):
        d = {}
        try:
           datei = open(Datei)
           liste = datei.readlines()
           for eintrag in liste:
                l_eintrag = eintrag.split()
                d[l_eintrag[0]] = l_eintrag[1:]
           datei.close()
        except:
            pass
        return d
    def Ändern(self):
        Korrektur1 = input("Geben Sie das Englische Wort das Sie ersetzen wollen\n")
        Korrektur2 = input("Wie lautet die neue Übersetzung\n")
        Vokabeln = self.ErschaffeDict()
        Vokabeln[Korrektur1] = Korrektur2
        r = open(self.Datei,"w")
        r.write(str(Vokabeln))
        b=input("Wollen Sie weitere Änderungen vornehmen\n?")
        if b == "ja":
            Ändern()
            return Vokabeln
        else:
            print("Spiel beginnt")
    def CheckUnit(self):
        r=input("Wollen Sie die Vokabel der Units überprüfen?\n")
        if r == "ja":
            s = int(input("Welches UNit soll überprüft werden?"))
            print("Die eingegebenen Vokabeln lauten:")
            Vokabeln = self.ErschaffeDict("Unit"+str(s)+"txt")
            print (Vokabeln)
            self.Ändern()
        else:
            print ("Spiel beginnt")
    def WahlUnit(self):
        k = input("Sollen alle Vokabel abgefragt werden?")
        if k == "ja":
            d={}
            for i in range(int(self.Anzahl)):
                 d.update(self.ErschaffeDict("Unit"+str(i)))
            return d
        else:
            d={}
            for i in range(int(self.Anzahl)):
                r = input("Wählen Sie UNit"+str(i)+"?")
                if r == "ja":
                    d = self.AddDict(d,ErschaffeDict("Unit"+str(i)))
            return d
    def legeNachHinten(self,Dict):
        Dict.append(Dict[0])
        del Dict[0]
    def Optionen(self):
        print( "\n[1] Jetzt nochmal versuchen.\n[2] Später nochmal abfragen.")
        return input("\nEnter option number: ").strip().lower()
    def Antwort(self,Wort,Liste):
        h = "\n[%s Fragen bleiben übrig]"% len(Liste.items())
        print(h)
        b = "\nWas ist die Übersetzung von: %s" % Wort
        print(b)
        return input("Übersetzung: \n").strip().lower()
    def EntferneSchlüssel(self,d, key):
        r = dict(d)
        del r[key]
        return r
    def Abfragen(self,Dict):
        Schlüssel_liste = list(Dict.keys())
        random.shuffle(Schlüssel_liste)
        Richtig = 0
        Falsch = 0
        for Schlüssel in Schlüssel_liste:
            Antwort1 = self.Antwort(Schlüssel,Dict)
            if Antwort1 == Dict[Schlüssel]:
                print("Richtige Antwort!")
                Richtig += 1
                Dict.pop(Schlüssel)
            else:
                print("Die Antwort war leider falsch")
                Falsch += 1
                while True:
                    option = self.Optionen()
                    if option == '1':
                        if self.Antwort(Schlüssel, Dict) == Dict[Schlüssel]:
                            print("Richtige Antwort!")
                            Richtig += 1
                            Dict = self.EntferneSchlüssel(Dict,Schlüssel)
                            break
                        else:
                            Falsch += 1
                            print("Die Antwort war leider falsch")
                    elif option == "2":
                        Dictneu = {}
                        Dictneu[Schlüssel]= Dict[Schlüssel]
                        Dict = self.EntferneSchlüssel(Dict,Schlüssel)
                        break
        self.Abfragen(Dictneu)
        sf = "Richtige Antworten --> {} Richtig und {} Falsch"
        print(sf.format(Richtig,Falsch))
