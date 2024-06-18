def cadastro_senha():
    senha =  input("Cadastre sua senha: ")
    return senha

def inicializar_celular(senha_cadastrada):
    senha_digitada = input("Digite sua senha para inicializar seu celular: ")
    
    if senha_digitada == senha_cadastrada:
        print("Senha correta. Bem-vindo!")
    else:
        print("Senha incorreta. Tente novamente.")

def simulador_cadastro_inicializacao():
    
    print("Bem-vindo! Para iniciar, vamos cadastrar uma senha.") 
    senha_cadastrada = cadastro_senha()    
    
    print("\nÓtimo! Agora digite sua senha para inicializar seu celular.")
    inicializar_celular(senha_cadastrada)
    
simulador_cadastro_inicializacao()         

