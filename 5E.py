consumo = int(input())

preco = 7
if consumo > 10 and consumo <= 30:
        preco += (consumo-10)*1
elif consumo > 30 and consumo <= 100:
        preco += (consumo-20)*2
elif consumo > 101:
        preco += (consumo-30)+((consumo-100)*2)*5


print(preco)