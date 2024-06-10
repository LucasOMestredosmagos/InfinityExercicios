import re
def solicitar_senha(mensagem):
    
    senha = input(mensagem)
    
    
    if not senha_valida(senha):
        print("\033[31m\033[1mA senha não atende aos requisitos mínimos. Tente novamente.\033[0m")
        return solicitar_senha(mensagem)
    else:
        return senha

def senha_valida(senha):
    
    if len(senha) <= 0:
        return False
    
   
    if not re.search(r'[a-zA-Z]', senha) or \
       not re.search(r'\d', senha) or \
       not re.search(r'[!@#$%^&*()_+{}|:"<>?~\-\[\]\\;\',./]', senha):
        return False
    
    return True     

def confirmar_senha():
    
    largura = 52
    titulo = "-Sistema de Cadastro de senha-".center(largura)
    print("=" * largura)
    print(titulo.ljust(largura))
    print("=" * largura)
    print("Por favor, cadastre uma senha que atenda aos seguintes requisitos:")
    print("\033[32m-\033[0m Pelo menos 8 caracteres".ljust(largura))
    print("\033[32m-\033[0m Inclua letras \033[1m(maiúsculas e minúsculas)\033[0m, números e símbolos".ljust(largura))
    print("Exemplo de senha forte: \033[1m@abc47#!\033[0m".ljust(largura))
    print("=" * largura)
    
    senha = solicitar_senha("Digite a nova senha: ")
    confirmar_senha = solicitar_senha("Confirme a nova senha: ")
    
    if senha == confirmar_senha:
        print("=" * largura)
        print("\033[92mSenha cadastrada com sucesso.\033[0m".ljust(largura))
        print("=" * largura)
        return senha
    else: 
        print("=" * largura)
        print("\033[91mAs senhas não coincidem. Tente novamente.\033[0m".ljust(largura))
        print("=" * largura)
        return confirmar_senha()
    
    
def autenticar_senha(Senha_cadastrada):
    largura = 52
    tentativas = 3
    
    while tentativas > 0:
        senha = solicitar_senha("Insira sua senha: ")
        
        if senha == Senha_cadastrada:
            print("=" * largura)
            print("\033[92mSenha correta. \033[34mBem-vindo(a).\033[0m".ljust(largura))
            print("=" * largura)
            return True
        else:
            tentativas -= 1
            print("=" * largura)
            print(f"\033[91mSenha incorreta. Você tem mais {tentativas} tentativa(s).\033[0m".ljust(largura))
            print("=" * largura)
    
    print("=" * largura)        
    print("\033[91mNúmero de tentativas excedido. Tente novamente daqui a 3 minutos.\033[0m".ljust(largura))
    print("=" * largura)
    return False

def main():
    
    largura = 52
    print("=" * largura)
    print("\033[36m\033[1mBem-vindo ao sistema de cadastro e autenticação de senha.\033[0m".ljust(largura))
    print("=" * largura)
    senha_cadastrada = confirmar_senha()
    
    if autenticar_senha(senha_cadastrada):
        print("\033[1mAutentificação bem-sucedida.\033[0m".ljust(largura))
    else:
        print("\033[43m\033[1mFalha na autenticação.\033[0m".ljust(largura))
if __name__ == "__main__":
    main()                    