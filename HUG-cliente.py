#Bibliotecas usadas
import string
import random
import socket
import threading

print("Seja bem vindo ao HUG!\nAqui você conhece pessoas novas e faz novas amizades :)\n")

def cadastro():
    nome = input("Insira seu nome:").lower()
    idade = input("Digite a sua idade: ").lower()
    senha = input("Insira uma senha: ").lower()
    #Gerador de Id usando os módulos string e random 
    def Id():
        s=string.ascii_uppercase+string.digits
        global identificacao
        identificacao = ''.join(random.sample(s,6)) #Join() serve para iterar ou seja reune todos os items e os coloca em um lugar no caso uma string
        return 
    Id()

    dados = open(f"dados_dos_usuarios\{nome}.txt", "w")
    dados.write(f"{nome} , {senha} , {idade} , {identificacao}\n")
    dados.close()

    print("\nCadastro realizado com sucesso! Agora você já pode se divertir com o HUG.\n")

#Essa função serve para confirma se você já temm uma conta ou não 
def login():
    global Nome
    Nome = input("Digite seu nome ou apelido:\n").lower()
    Senha = input("Digite a senha para efetuar o login:\n").lower()

    leitor = open(f"dados_dos_usuarios\{Nome}.txt", "r")
    for lista in leitor: 
        global valores
        valores = lista.split()  
    print("\nOh que ótimo! Vamos prosseguir.\n")


loginOuCadastro = input("Como primeiro passo, é necessário fazer um cadastro. Mas se já usou o Hug efetue o login.\nPara login digite [1];\nPara cadastro dígite [2]:\n")

if (loginOuCadastro) == '1':    
    login()
elif (loginOuCadastro) == '2':
    cadastro()
else:
    #Estrátegia para bloquear a entrada de possíveis intrusos.
    print("Por segurança, estamos encerrando o programa. Você só pode acessá-lo se tiver uma conta.\n")
    quit()

entrarNoServidor = input("Você quer entrar no servidor?").lower()
if entrarNoServidor == 'sim':
    #Parte do cliente usando os modulos socket e threading a conexão entre cliente e servidor é feita via socket.
    apelido = valores[0]

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('127.0.0.1', 55555))
    #Essa função após conectado o servidor serve como o nome já diz receber e enviar dados de como o servidor está e para manter o servidor atualizado.
    def receber():
        while True:
            try:
                mensagem = cliente.recv(1024).decode('ascii')
                if mensagem == "NICK":
                    cliente.send(apelido.encode('ascii'))
                else:
                    print(mensagem)
            except:
                print("Desculpe-nos! Um erro aconteceu!")
                cliente.close()
                break           
                #função de envio de mensagem, é um while que sempre ativo recebe um input e mostra na tela com a função send().
    def escrever():
        while True:
            mensagem = f"{apelido}: {input('')}"
            cliente.send(mensagem.encode('ascii'))
elif entrarNoServidor == 'não':
    quit()
#Os threads são da biblioteca threading aqui é onde o programa essas funções receber() e escrever() são executadas.
threadReceber = threading.Thread(target=receber)
threadReceber.start()

threadEscrever = threading.Thread(target=escrever)
threadEscrever.start()


