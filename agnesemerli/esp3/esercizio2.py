
n = int(input("inserisci numero intero "))
n_bit =int(input("inserisci numero di bit "))

print("\n in binario: ", bin(n))
print(" in esadecimale: ", hex(n))
nshift1= n >> n_bit
nshift2= n << n_bit
print(f"\n in decimale shiftato a dx di {n_bit} bit :", nshift1 )
print(f"\n in binario shiftato a dx di {n_bit} bit :", bin(nshift1))
print(f"\n in esadecimale shiftato a dx di {n_bit} bit: ", hex(nshift1))
print(f"\n in decimale shiftato a sx di {n_bit} bit: ", nshift2 )
print(f"\n in binario shiftato a sx di {n_bit} bit: ",bin(nshift2))
print(f"\n in esadecimale shiftato a sx di  {n_bit} bit: ", hex(nshift2))

