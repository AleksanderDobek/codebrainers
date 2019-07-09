import random  




wytypowane = set()


wylosowane = set()
while (not len(wylosowane) == 6):
    wylosowane.add(random.randint(1, 49))  # niebezpieczna pętla bo jak ktoś wpowadźi jedną liczbę to w nieskończoność
   
#sample(range(50), liczba=1):
kolejno_wytypowana = 1 
while kolejno_wytypowana <= 6:  
    liczba = input(f"Podaj {kolejno_wytypowana} liczbe:")
    if (liczba.isdigit()):
        liczba = int(liczba)
        if liczba >= 1 and liczba < 50:
            if liczba not in wytypowane:
                wytypowane.add(liczba)
                kolejno_wytypowana += 1
            else:
                print("Już podawales te liczbe. Wybierz inna!")
        else:
            print("Możesz podawać tylko liczby z przedziału 1 - 49")  
    else:
        print("Muszisz podawac tylko liczby!")    
        

print(" Wylosowane liczby to : ",wylosowane) 

print(" Twoje typy to: ",wytypowane)

print("Trafiłeś: ", len(wytypowane & wylosowane), "z", len(wylosowane))









#for liczba in wylosowane:
    #print(liczba)
    #podana = input("podaj zwycięzkie liczby: ")










#proba = 0
#zgadywana = 0
#znaki = ra
#while not zgadl:
    #zgadywana  = input("podaj liczbe: ")
    #if(zgadywana.isdigit()):  #funkcja ktora dziala na stringu
        #zgadywana = int(zgadywana)
        #proba+=1
        #if proba == 6:
            #print('Uwaga masz ostatn szansę')
        #if proba >= 7:
            #print('próba numer', proba, 'przegrałes')
           # break
        #if zgadywana == liczba:
           # print('brawo zgadłes za', proba, 'razem') 
            #break       
        #if zgadywana > liczba:
            #print('za wysoko', proba, 'próba')
        #if zgadywana < liczba:
            #print('za nisko', proba, 'próba')
        #if  zgadywana > 101:
            #print('NIE OSZUKUJ !!! tylko liczby od 1 101')
        #elif zgadywana < 1:
           # print('NIE OSZUKUJ !!! tylko liczby od 1 101')
           # break
   # else:
       # print("Muszisz podac liczbe! Nie marnujesz proby")