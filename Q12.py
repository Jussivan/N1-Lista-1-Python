numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
impares = []
for num in numeros_lista:
    if int(num) % 2 != 0:
        impares.append(int(num))
print("Números ímpares: ", impares)