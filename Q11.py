numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
pares = []
for num in numeros_lista:
    if int(num) % 2 == 0:
        pares.append(int(num))
print("Números pares: ", pares)