numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
maiores_que_10 = []
for numero in numeros_lista:
    if int(numero) > 10:
        maiores_que_10.append(numero)
print("Números maiores que 10: ", maiores_que_10)
