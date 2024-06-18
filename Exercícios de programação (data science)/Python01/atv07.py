#Verificação de Vogal ou Consoante

letra = input("Digite uma letra: ").lower()  

if letra.isalpha() and len(letra) == 1:  
    if letra in 'aeiou':
        print(f'A letra "{letra}" é uma vogal.')
    else:
        print(f'A letra "{letra}" é uma consoante.')
else:
    print('Por favor, digite apenas uma letra do alfabeto.')
    
#Cálculo da Média de Notas e Avaliação do Aluno 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f'Média: {media:.2f}')

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")