import math
a = float(input("Qual o valor de a: "))
b = float(input("Qual o valor de b: "))
c = float(input("Qual o valor de c: "))

delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

if delta > 0:
    print("Duas raízes reais distintas",x1,"e",x2)
elif delta == 0:
    print("Uma única raiz real",x1 or x2)
elif delta < 0:
    print("Duas raízes complexas")