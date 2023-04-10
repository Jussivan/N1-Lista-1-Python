numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
menores_que_5 = []
for numero in numeros_lista:
    if int(numero) < 5:
        menores_que_5.append(numero)
print("Números menores que 5: ", menores_que_5)