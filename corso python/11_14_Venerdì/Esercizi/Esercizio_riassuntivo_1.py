""" 
    Creare una funzione che prende un intero positivo per generare una sottolista dei primi n elementi di una lista definita dall'utente, inoltre la funzione deve far scegliere se restituire la sottolista, eliminare i duplicati o verificare le eventuali differenze tra la lista e la sottolista.
"""
#funzione per eseguire le funzionalità dell'esercizio
def allInOne (n, list):
    
    #inizializzazione nuova lista
    new_list = []
    end = 0
    
    #riempio la nuova lista
    while end < n:
        new_list.append(list[end])
        end +=1
    
    #scelta dell'operazione
    chooice = int(input("Scegliere una delle seguenti operazioni: \n 1. Restituire la sottolista \n 2. Eliminare i duplicati della sottolista\n 3. Verificare gli elementi diversi della sottolista \n"))
    
    match chooice:
        case 1:
            return new_list
        case 2:
            #conversione per eliminare i duplicati
            list_without_double = set(new_list)
            return list_without_double
        case 3:
            #vedere perchè mi ritorna set() e non la differenza 
            set_new = set(new_list)
            print(set_new)
            set_ori = set(list)
            print(set_ori)
            return set_new.difference(set_ori)
        case _:
            return False
    
x = allInOne(4, [9, 2, 2, 4, 5, 1, 3, 4])

print(x)