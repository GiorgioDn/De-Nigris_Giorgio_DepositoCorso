from Esercizio_riassuntivo_1 import *

def d_controllo_negativi(funzione):
    def wrapper(*args, **kwargs):
        if args[0]<0:
            args[0] = abs(args[0])
        result = funzione(*args, **kwargs)
        return result
    return wrapper

def d_controllo_lista(funzione):
    def wrapper(*args, **kwargs):
        if len(args[1]) !=0:
            if funzione.__name__ == "":
                result = funzione(*args, **kwargs)
                return result
        else:
            if funzione.__name__ == "":
                result = funzione(*args, **kwargs)
                return result
    return wrapper