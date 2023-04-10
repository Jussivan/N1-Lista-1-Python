numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
soma_numeros = 0
for num in numeros_lista:
    soma_numeros += float(num)
media = soma_numeros / len(numeros_lista)
print("A média dos números é : ", media)