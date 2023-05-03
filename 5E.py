def calcular_valor_conta_agua(consumo):
    valor_total = 7  # Valor da assinatura básica

    if consumo > 10:
        if consumo <= 30:
            valor_total += (consumo - 10) * 1
        elif consumo <= 100:
            valor_total += 20  # Valor para o intervalo de 11 a 30m3
            valor_total += (consumo - 30) * 2
        else:
            valor_total += 20  # Valor para o intervalo de 11 a 30m3
            valor_total += 70 * 2  # Valor para o intervalo de 31 a 100m3
            valor_total += (consumo - 100) * 5

    return valor_total


consumo = int(input())  # Leitura do consumo de água da residência
valor_conta = calcular_valor_conta_agua(consumo)
print(valor_conta)
