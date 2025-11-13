#faccio selezionare all'utente i due numeri per lo step ed il massimo
print("Scegliere il numero massimo, gli step del range ed i numeri visualizzati per riga")
max = int(input("Massimo: "))
step = int(input("Step: "))
row = int(input("Numeri per riga: "))

counter = 0

#controllo che il massimo sia maggiore degli step
if max>step:
    #stampo i numeri per riga definiti dall'utente fino al massimo
    for i in range(0, max + 1, step):
        print(i, end=" ")
        counter += 1
        if counter == row:
            #vado a capo
            print()    
            counter = 0
else:
    print("Dati non validi")