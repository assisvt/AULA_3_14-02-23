valor = int(input("Digite um número: "))
if valor >= 100:
    print("O valor é maior ou igual a cem.")
else:
    print("Valor menor do que cem.")
print("Ademais, o valor que você escolheu foi:", valor)
--
# Faça um programa que calcule a média aritmética de um aluno que realizou duas avaliações.
# Além do valor da média, inclua na tela de saída uma das menssagens: "Aluno aprovado." ou "Aluno reprovado."
# aprovado: maior ou igual a 5
# reprovado: menor do que 5
nota1 = float(input("Qual foi a sua nota na primeira prova? "))
nota2 = float(input("Qual foi a sua nota na segunda prova? "))
media = (nota1 + nota2)/2 #parênteses obrigatórios
if media >= 5:
    print(f'Aluno aprovado com média = {media:.2f}')
else:
    print(f'Aluno reprovado com média = {media:.2f}')
# ALTERAÇÕES: mostre o valor da média aritmética com duas casas decimais
--
# Solução 1
# Elabore o programa que verifica se o valor inteiro fornecido pelo usuário é par ou ímpar.
# Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
valor = int(input("Digite um número: ")) # receba o número digitado
resto = valor % 2 # pega o resto da divisão de dois números
if resto == 0: # verifica se o valor da variável resto = 0, se o número é par
    print("Número par.")
else: #caso contrário
    print("Número ímpar.")
 --
# solução 2 (mais formaado/resumido)
valor = int(input("Digite um número: "))
if valor % 2 == 0:
    print(f"O número {valor} é par")
else:
    print(f"Número {valor} é ímpar.")
