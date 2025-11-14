from Esercizio_riassuntivo_1 import *

#controlla il parametro della funzione e se è negativo lo fa diventare positivo
def d_controllo_negativi(funzione):
    def wrapper(*args, **kwargs):
        if args[0]<0:
            new_args = list(args)
            new_args[0] = abs(new_args[0])
            result = funzione(*new_args, **kwargs)
        else: 
            result = funzione(*args, **kwargs)
        return result
    return wrapper

#eseguire la funzione in base alla lista
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
