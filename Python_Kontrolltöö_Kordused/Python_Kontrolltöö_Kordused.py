from random import *
from math import *
#4 Võimalus
#1.
print()
n=randint(1,9)                      # sisestab juhusliku arvu
print("n")
while n!=1:                    # Silmuse abil kuvame mitu kujundit
   print("  ^---^")          #kujundite kuvamine tühikutega
   print(" ( o o )")
   print("  ! = !/)")
   print()
   n=0

#4
for i in range(1,9):                    #silmuse korpus
    print(f"{i*3}",end=" ")              #kuvab reas, mitu korda omeba on 24 tunni jooksul jaganud

#3.2
õpilane1 =int(input("sisestage hinded järjest: "))      #pane hinded järjest
õpilane2 = int(input("sisestage hinded järjest: "))
õpilane3 = int(input("sisestage hinded järjest: "))

sõnad = [õpilane1, õpilane2, õpilane3]
pikim_sõna = max(sõnad, key=len)                #key=len - aitab määrata miinimum- ja maksimumhinde
lühim_sõna = min(sõnad, key=len)

print(f"Kõige pikem sõna: {pikim_sõna}")        #maksimaalse ja minimaalse punktisumma kuvamine
print(f"Kõige lühem sõna: {lühim_sõna}")


#2.
a=int(input("Sisesta astendaja: "))
n=int(input("Sisestage number n"))
b=1
v=0
while b<=n*100:
    print(f"{n}")


#3.1
a=int(input("Sisestage õpilaste arv"))
x=[randint(1,10) for i in range(a)]
min_1=min(x)
max_1=max(x)
print("Minimaalsed hinded {min_1}")
print("Maksimaalsed hinnangud {max_1}")        
