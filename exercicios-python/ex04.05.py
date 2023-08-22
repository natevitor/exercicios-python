# Exercicio 4
# Escreva um programa que receba um afrase como uma entrada e retorne uma lista das 
# palavras presentes na frase 
def lista_palavras (frase):
    return frase.split (' ')

#Exercicio 5 
# Implemente uma função que retorne a quantidade de palavras existentes em uma string 
def conta_palavras(frase):
    lista = frase.split(' ')
    return len(lista)

frase = input ('Frase:')
print(lista_palavras(frase))
print(conta_palavras(frase))
