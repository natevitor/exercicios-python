lista1 = []
lista2 = []


for i in range (5):
    n = int(input('Numeros'))
    lista1.append(n)


for i in range (5): #preenche a lista 
    n = int (input('Numeros'))
    lista2.append(n)

tupla1 = tuple (lista1)   #copia as listas para tuplas 
tupla2 = tuple (lista2)       


tupla3 = tupla2 + tupla2
print(tupla3)