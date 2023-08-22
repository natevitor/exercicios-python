# Preencha uma lista com 10 numeros inteiros e exibir:
# o maior, o menor e a media dos numeros

# preenche a lista com 10 numeros 
lista = []
for i in range (10):
    numero = int (input('Numero'))
    lista.append(numero)
print(lista)

maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {media}')