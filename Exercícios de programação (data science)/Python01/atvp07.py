def maior_numero():
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    n3 = float(input("Informe o terceiro número: "))

    maior = max(n1, n2, n3)
    print(f"O maior número é: {maior}")

maior_numero()

def maior_e_menor():
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    n3 = float(input("Informe o terceiro número: "))
    
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    
maior_e_menor()

def produto_mais_barato():
    preco1 = float(input("Informe o preco do primeiro produto: "))  
    preco2 = float(input("Informe o preco do segundo produto: ")) 
    preco3 = float(input("Informe o preco do terceiro produto: "))   
    
    mais_barato = min(preco1, preco2, preco3)
    
    if mais_barato == preco1:
        print("Você deve comprar o primeiro produto.")
    elif mais_barato == preco2:
        print("Você deve comprar o segundo produto.")
    else:
        print("Você deve comprar o terceiro produto.")  
        
produto_mais_barato()   

def ordem_decrescente():
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    n3 = float(input("Informe o terceiro número: "))
    
    numeros = [n1, n2, n3]
    numeros.sort(reverse=True)
    
    print("Os números em ordem decrescente são:", numeros)
    
ordem_decrescente()    
   
    