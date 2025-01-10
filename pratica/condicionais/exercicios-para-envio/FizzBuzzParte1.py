numero = int(input("Digite o número: "))

#soma = sum(int(digito) for digito in str(numero)) # Faz o somatório do número recebido na variável número
if numero % 3 == 0:
    print("Fizz")
else:
    print(numero)

#print(f'A soma de {numero} é {soma}')