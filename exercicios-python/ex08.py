#Preencher um a lista com 10 numeros 
#
#



#preenche a lista com 10 numeros 
lista = []
for i in range (10):
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

cont = 0 
soma = 0 
for item in lista:
    if item % 2 == 0:
        cont += 1   #conta os pares
    else: 
        soma += item # soma os pares     

print(f'Quantidade de Pares: {cont}')        
print(f'Somatório dos Ímpares:{soma}')