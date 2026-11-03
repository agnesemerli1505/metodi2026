import numpy as np 
import somme

n= int(input("scegli un numero naturale :"))
s, p = somme.somma(n)
print(f"la somma dei primi {n} numeri naturali è ", s)
print(f"il prodotto dei primi n numeri naturali è ", p)

r=somme.somma_radice(n)
print(f"la somma delle radici dei primi {n} numeri naturali è ", r) 
alfa=int(input("scegli un numero tra uno e 5 "))
pot=somme.somma_potenze(n, alfa)
print(f"la somma dei primi {n} numeri naturali elevati ad {alfa} è ", pot)


