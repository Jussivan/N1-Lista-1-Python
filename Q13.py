palavras = input("Digite uma lista de palavras separadas por vírgula: ")
palavras_lista = palavras.split(",")
a_palavras = []
for palavra in palavras_lista:
    if palavra[0].lower() == "a":
        a_palavras.append(palavra)
print("Palavras que começam com 'a': ", a_palavras)