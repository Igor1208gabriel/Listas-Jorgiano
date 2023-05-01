a = int(input())
b = int(input())
c = int(input())
d = int(input())

lista = a,b,c,d
lista = sorted(lista)

um = lista[3]+lista[0]
dois = lista[2]+lista[1]

print(abs(um-dois))