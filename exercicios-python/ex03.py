def conta_vogais(frase):
    frase = frase.lower()
    quantidade = frase.count('a')
    quantidade = frase.count('b')
    quantidade = frase.count('c')
    quantidade = frase.count('d')
    quantidade = frase.count('e')
    return quantidade


def conta_vogais2(frase):
    frase = frase.lower()
    quantidade = 0
    for caracter in frase:
        if caracter in 'aeiou':
            quantidade += 1
    return quantidade 


frase = input ('Frase: ')
print (conta_vogais(frase))
print (conta_vogais2(frase))
    
    

    