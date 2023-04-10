numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_lista = numeros.split(",")
numeros_lista = [int(x) for x in numeros_lista] # converte a lista de strings para lista de inteiros
numeros_lista.sort(reverse=True) # ordena a lista em ordem decrescente
print("A lista em ordem decrescente é:", numeros_lista)