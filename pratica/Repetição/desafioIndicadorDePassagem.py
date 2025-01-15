# Dado um número, o programa tem que dizer se tem dois números iguais adjacentes.

numero = int(input("Digite a sequência de números: "))
anterior = -1
repetido = False

while numero > 0:
    atual = numero % 10
    if atual  == anterior:
        repetido = True
        break
    anterior = atual
    numero //= 10

if repetido:
    print("Sequencia tem números repetidos adjacentes")
else:
    print("Sequência de números sem repetições adjacentes")