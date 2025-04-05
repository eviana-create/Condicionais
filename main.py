temperatura = int(input("Digite Temperatura: "))
if temperatura >= 100:
    aguaFerve = True
    evaporacao = "Muito Rapido"
    print("Agua ferve", aguaFerve, evaporacao)
else:
    print("Agua não esta quente")
    aguaFerve = False
    evaporacao = "Agua Fria"
    print(aguaFerve, evaporacao)