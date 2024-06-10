def verificar_valor():
    valor = float(input("Por favor, informe um valor: "))
    
    if valor > 0:
        print("O valor é positivo.")
    elif valor < 0:
        print("O valor é negativo.")
    else:
        print("O valor é zero.")

verificar_valor()
