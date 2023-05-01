comida1, comida2, comida3 = map(int, input().split())
quero1, quero2, quero3 = map(int, input().split())

falta1 = comida1-quero1
falta2 = comida2-quero2
falta3 = comida3-quero3

faltam = 0
if falta1 < 0:
    faltam += falta1
if falta2 < 0:
    faltam += falta2
if falta3 < 0:
    faltam += falta3

print(abs(faltam))