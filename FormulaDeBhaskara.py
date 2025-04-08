import math
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz é: ", raiz1)

else:
    if delta < 0:
        print("Esta equação não possui raizes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é: ",raiz1)
        print("A segunda raiz é: ",raiz2)