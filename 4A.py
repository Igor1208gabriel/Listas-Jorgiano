preco_alc, preco_gas, kml_alc, kml_gas = map(float, input().split())
 
valor_alc = preco_alc / kml_alc
valor_gas = preco_gas / kml_gas
 
if valor_gas <= valor_alc: print("G")
else: print("A")
