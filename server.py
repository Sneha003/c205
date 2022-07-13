from asyncio import Handle
from pickle import NONE
import socket
from threading import Thread

SERVER=None
PORT=None
IP_ADDRESS=None



CLIENTS={}
def HandleClients(player_socket,player_name):
    global CLIENTS


    playerType =CLIENTS[player_name]["player_type"]
    if(playerType== 'player1'):
        CLIENTS[player_name]['turn'] = True
        player_socket.send(str({'player_type' : CLIENTS[player_name]["player_type"] , 'turn': CLIENTS[player_name]['turn'], 'player_name' : player_name }).encode())
    else:
        CLIENTS[player_name]['turn'] = False
        player_socket.send(str({'player_type' : CLIENTS[player_name]["player_type"] , 'turn': CLIENTS[player_name]['turn'], 'player_name' : player_name }).encode())

    while True:
        try:
            message = player_socket.recv(2048)
            if(message):
                for cName in CLIENTS:
                    cSocket = CLIENTS[cName]["player_socket"]
                    cSocket.send(message)
        except:
            pass
def addConnection():
    global CLIENTS
    global SERVER
    while True:
        player_socket,addr=SERVER.accept()
        player_name=player_socket.recv(1024).decode().strip()
        if(len(CLIENTS.keys())==0):
            CLIENTS[player_name]={"player_type":"player1"}
        else:
            CLIENTS[player_name]={"player_type":"player2"}
        CLIENTS[player_name]["player_socket"]=player_socket
        CLIENTS[player_name]["address"]=addr
        CLIENTS[player_name]["player_name"]=player_name
        CLIENTS[player_name]["turn"]=False

        print(f"Connection established with{player_name}:{addr}")

        thread=Thread(target=HandleClients,args={player_socket,player_name})
        thread.start

def setup():
    print("\n")
    print("\t\t\tLUDO LADDER ****")

    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 8000

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)

    print("t\t\tSERVER IS WAITING FOR INCOMING CONNECTION")
    print("\n")
setup()


