import random  
liczba = random.randint(1, 101)
zgadl = False
proba = 0
zgadywana = 0
while not zgadl:
    zgadywana = int(input("podaj liczbe: "))
    proba+=1
    if proba == 6:
        print('Uwaga masz ostatnią szansę')
    if proba > 7:
        print('próba numer', proba, 'przegrałes')
        break
    if zgadywana == liczba:
        print('brawo zgadłes za', proba, 'razem') 
        break   
    if zgadywana > liczba:
        print('za wysoko', proba, 'próba')
    if zgadywana < liczba:
        print('za nisko', proba, 'próba')
    if  zgadywana > 101:
        print('NIE OSZUKUJ !!! tylko liczby od 1 101')
    elif zgadywana < 1:
        print('NIE OSZUKUJ !!! tylko liczby od 1 101')
   