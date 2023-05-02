linha=int(input())
coluna=int(input())
 
if linha % 2 == 0:
    linha_par = True
elif linha % 2 > 0:
    linha_par = False
 
if coluna % 2 == 0:
    coluna_par = True
elif coluna % 2 > 0:
    coluna_par = False
 
if linha_par == coluna_par:
    parimpar = 1
else:
    parimpar = 0
print(parimpar)
