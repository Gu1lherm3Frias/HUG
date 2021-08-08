# -*- coding: utf-8 -*-
import socket
import threading
import mysql.connector
import databaseconnection

importlib.import_module(database-connection)


host = '127.0.0.1'
port = 55564

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []

def transmission(mensagem):
    for client in clients:
        client.send(mensagem)

def connection(client):
    while True:
        try:
            message = client.recv(1024)
            transmission(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            transmission(f"{name} exit of chat!".encode(ascii))
            names.remove(name)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"\nConnected with {str(address)}\n")

        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        print(f"\nClient name is {name}\n")
        transmission(f"\n{name} joined to the chat !\n".encode('ascii'))
        client.send('\nConnected to Chat!\n'.encode('ascii'))

        thread = threading.Thread(target=connection, args=(client,))
        thread.start()

print("Server is Online...")
receive()