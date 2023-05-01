um,dois,tres,quatro = map(int, input().split())
 
 
if um + dois > tres and um + tres > dois and tres + dois > um:
    print("S")
elif um + dois > quatro and um + quatro > dois and dois + quatro > um:
    print("S")
elif um + tres > quatro and um + quatro > tres and quatro + tres > um:
    print("S")
elif dois + tres > quatro and dois + quatro > tres and tres + quatro > dois:
    print("S")
else:
    print("N")
