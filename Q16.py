numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
soma_pares = 0
for numero in numeros_lista:
    if int(numero) % 2 == 0:
        soma_pares += int(numero)
print("A soma dos números pares é:", soma_pares)