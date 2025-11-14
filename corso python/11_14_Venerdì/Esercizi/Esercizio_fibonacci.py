#importo tutte le funzioni presenti nel file Fibonacci.py
from Fibonacci import *
        
while True:
    #chiedo il numero della sequenza
    num_fibonacci = int(input("Digitare un numero intero positivo per la sequenza di fibonacci: "))
    #inizializzo la lista con i risultati
    lista_res = []
    result = fibonacci_succ(num_fibonacci, lista_res)
    print(result)
    
    chooice = input("Si desidera continuare ad inserire numeri? ")
    
    if chooice.lower() == "no":
        break
