indicador1, distancia1, velocidade1 = map(int, input().split())
indicador2, distancia2, velocidade2 = map(int, input().split())
 
tempo1 = distancia1 / velocidade1
tempo2 = distancia2 / velocidade2
 
if tempo1 > tempo2: print(indicador2)
elif tempo2 > tempo1: print(indicador1)
