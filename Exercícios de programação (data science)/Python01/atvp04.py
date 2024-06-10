def imprimir_maior_numero():
    n1 = float(input("Por favor, informe o primeiro número: "))
    n2 = float(input("Por favor, informe o segundo número: "))
    
    if n1 > n2:
        print(f"O maior número é: {n1}")
    elif n2 > n1:
        print(f"O maior número é: {n2}")
    else:
        print("Os dois números são iguais.")    
imprimir_maior_numero()            
