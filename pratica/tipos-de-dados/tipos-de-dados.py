# Para saber o tipo de dado, usamos type(variável). Por exemplo:

x = 10
print(type(x))

frase = "tudo bem?"
print(type(frase))

divisao = 5/2
print("O resultado de 5/2 é", divisao, "e o seu tipo é:", type(divisao))

divInteira = 10//3
print("O resultado da divisão inteira 10/3 é", divInteira, "e o seu tipo é:", type(divInteira))

restoDiv = 10 % 3
print("O resto da divisão 10/3 é", restoDiv, "e o seu tipo é: ", type(restoDiv))

print("--------------------------------------------------------------------------------")

nome = "João"
peso = 78
altura = 1.83
imc = peso / (altura ** 2)
imcInteiro = int(imc) # Converter o tipo float para o tipo inteiro
print("O paciente", nome, "possui o", peso, "Kg, a altura", altura, "e seu IMC é:", imc, "e o valor inteiro do IMC é:", imcInteiro)

print("--------------------------------------------------------------------------------")

texto = "Bom dia tudo bem?"
print("O texto", texto, "possui", len(texto), "caracteres") #len(variável) conta quantos caracteres possui uma string

print("--------------------------------------------------------------------------------")