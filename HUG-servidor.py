import socket
import threading


hospedeiro = '127.0.0.1'
porta = 55555

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((hospedeiro, porta))
servidor.listen()

clientes = []
nomes = []

def transmissao(mensagem):
    for cliente in clientes:
        cliente.send(mensagem)

def ligaçao(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            transmissao(mensagem)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nome = nomes[index]
            transmissao(f"{nome} saiu do chat!".encode(ascii))
            nomes.remove(nome)
            break

def receber():
    while True:
        cliente, endereço = servidor.accept()
        print(f"\nConectou-se com {str(endereço)}\n")

        cliente.send('NICK'.encode('ascii'))    
        nome = cliente.recv(1024).decode('ascii')
        nomes.append(nome)
        clientes.append(cliente)

        print(f"\nNome do cliente é {nome}\n")
        transmissao(f"\n{nome} entrou no chat!\n".encode('ascii'))
        cliente.send('\nConectado ao servidor!\n'.encode('ascii'))

        thread = threading.Thread(target=ligaçao, args=(cliente,))
        thread.start()

print("servidor está ouvindo...")
receber()