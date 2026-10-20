import numpy
n1 = int(input("inserisci un numero intero: "))
n2 = int(input("inserisci un altro numero intero: "))

print("\nprimo numero: ")
print("binario ", bin(n1))
print("esadecimale ", hex(n1))

print("\nsecondo numero: ")
print("binario ", bin(n2))
print("esadecimale ", hex(n2))

ris_and = n1 & n2
ris_or = n1 | n2

print("\nrisultato and in binario : ", bin(ris_and))
print("risultato and in esadecimale : ", hex(ris_and))
print("\nrisultato or in binario: ", bin(ris_or))
print("risultato or in esadecimale : ", hex(ris_or))

