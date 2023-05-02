monitor = int(input())-1
alunos = int(input())
 
viagens = alunos//monitor
 
if alunos%monitor > 0:
    viagens = viagens+1
print(viagens)
