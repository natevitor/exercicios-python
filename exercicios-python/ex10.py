'''Preencha duas listas, uma para armazenar os nomes e outra para armazenar 
as idades de pessoas.
A entrada de dados deve ser finalizada quando o usuario informar um nome vazio.
Na sequencia informe o nome das pessoas que possuem idade igual ou superior a 
18 anos'''

nomes = []
idades = []

while True:
    nome = input('Digite um nome: ')
    if nome == '':
        break
    idade = int(input('Digite a idade: '))

    nomes.append (nome)
    idades.append (idade)
print(nomes)
print(idades)

for i in range (len(nomes)): #percorre os indices das listas 
    if idades[i] >= 18:
        print(nomes[i])