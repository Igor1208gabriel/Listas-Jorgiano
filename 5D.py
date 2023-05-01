monica = int(input())
filhoum = int(input())
filhodois = int(input())
filhotres = (filhoum*-1)+(filhodois*-1)+monica

if filhoum > filhodois and filhoum > filhotres: print(filhoum)
elif filhodois > filhoum and filhodois > filhotres: print(filhodois)
elif filhotres > filhoum and filhotres > filhodois: print(filhotres)

#soma idd filhos = monica