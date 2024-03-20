from utils import Hauptprogram

def Run():
    A = Hauptprogram()
    A.Units()
    A.CheckUnit()
    Dict = A.WahlUnit()
    A.Abfragen(Dict)
Run()