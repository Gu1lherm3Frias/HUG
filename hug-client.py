# -*- coding: utf-8 -*-
#Library used
import string
import random
import socket
import threading
import mysql.connector
from databaseconnection import *

print("Welcome to HUG cli chat\n")

# documentation for the code https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
def signin():

    sqlconnection = mysql.connector.connect(user=sqluser, password=sqlpassword, host=sqlhost, database=sqldatabase)

    intoname = input("Your username: ").lower()
    intoage = int(input("Which is your age?: ").lower())
    intopassword = input("Type a strong password with eight letters and numbers: ").lower()

    adduser = "insert into users (name,age,password) values (%s, %s, %s)"

    cursor = sqlconnection.cursor()
    cursor.execute(adduser, (intoname, intoage, intopassword))
    emp_no = cursor.lastrowid

    sqlconnection.commit()

    cursor.close()
    sqlconnection.close()

    print("\nSignup with Sucesses!\n")

#Essa função serve para confirma se você já temm uma conta ou não 
def login():
    global name
    name = input("Type your username: \n").lower()
    password = input("Type your password: \n").lower()

    reader = open(f"dados_dos_usuarios\{name}.txt", "r")
    for list in reader:
        global values
        values = list.split()
    print("\nOh que ótimo! Vamos prosseguir.\n")


loginOrSignin = input("You have a account? (y/n)")

if (loginOrSignin) == 'y':
    login()
elif (loginOrSignin) == 'n':
    signin()
else:
    #Estrátegia para bloquear a entrada de possíveis intrusos.
    print("Only accounts can chat, create one and try again.\n")
    quit()

joinToServer = input("You wanna join to chat? (y/n): ").lower()
if joinToServer == 'y':
    #Parte do cliente usando os modulos socket e threading a conexão entre cliente e servidor é feita via socket.
    nickname = values[0]

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55564))
    #Essa função após conectado o servidor serve como o nome já diz receber e enviar dados de como o servidor está e para manter o servidor atualizado.
    def receive():
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if message == "NICK":
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("Sorry, a error happned!")
                client.close()
                break           
                #função de envio de mensagem, é um while que sempre ativo recebe um input e mostra na tela com a função send().
    def write():
        while True:
            message = f"{nickname}: {input('')}"
            client.send(message.encode('ascii'))
elif joinToServer == 'n':
    quit()
#Os threads são da biblioteca threading aqui é onde o programa essas funções receber() e escrever() são executadas.
threadReceive = threading.Thread(target=receive)
threadReceive.start()

threadWrite = threading.Thread(target=write)
threadWrite.start()


