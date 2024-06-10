def soma_dois_numeros():
    n1 = float(input("Por favor, informe o primeiro número: "))
    n2 = float(input("Por favor, informe o segundo número: "))
    soma = n1 + n2
    print(f"A soma dos dois números é: {soma}")
    
soma_dois_numeros() 

def media_notas_bimestrais():
    notas =[]
    for i in range(1, 5):
        nota = float(input(f"Informe a nota do {i}º bimestre: "))
        notas.append(nota)
        media = sum(notas) / len(notas)
        print(f"A média das notas bimestrais é: {media}")

media_notas_bimestrais()  
         
def converter_metros_para_centímetros():
    metros = float(input("Por favor, informe a quantidade em metros: "))
    centimetros = metros * 100
    print(f"{metros} metros é igual a {centimetros} centímetros.")
    
converter_metros_para_centímetros() 

def area_dobro_quadrado():
    lado = float(input("Por favor, informe o tamanho do lado do quadrado (em metros): "))
    area = lado * lado
    dobro_area = area * 2 
    print(f"A área do quadrado é: {area} m² ")
    print(f"O dobro da área do quadro é: {dobro_area} m²")

area_dobro_quadrado()   

def calcular_salario_mensal():
    ganho_por_hora = float(input("Quanto você ganha por hora? "))
    horas_trabalhadas = float(input("Quantas horas você trabalhou no mês?  "))
    salario_mensal =  ganho_por_hora * horas_trabalhadas
    print(f"O total do seu salário no mês é: R$ {salario_mensal:.2f}")
    
calcular_salario_mensal()    

    
 
         