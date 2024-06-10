def verificar_sexo():
    letra = input("Por favor, informe uma letra (F ou M): ").strip().upper()  
    if letra == "F":
        print("F - Feminnino")
    elif letra == "M":
        print("M - Masculino")
    else:
        print("Sexo Inválido")  

verificar_sexo()              

#O método strip() é usado para remover espaços em branco no início e no fim da entrada, e upper() converte a letra para maiúscula para garantir que a verificação seja insensível a maiúsculas/minúsculas.