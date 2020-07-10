import socket
import argparse
import threading 

import Pyro4;

parser = argparse.ArgumentParser(description = "Servidor")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 7999)
args = parser.parse_args()

def saveClient(ip,port,mensagem):
    with open("./config/key.txt","r+") as f:
        key_uri = f.read();
    f.close();

    keyq = Pyro4.Proxy(key_uri);

    keyq.adicionaClients(ip,port,mensagem)

    

def Server():
    print(f"Configurações do SERVIDOR :\n----------------------------\n(IP): {args.host}\n(PORTA): {args.port}\n----------------------------")    

    sck = socket.socket()
    sck.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try: 
        sck.bind((args.host, args.port))
        sck.listen(5)
    except Exception as e:
        raise SystemExit(f"Erro : IP/Porta em uso ou inválidos!")
    while True:
        client, ip = sck.accept()
        threading._start_new_thread(client_connection,(client, ip))
	
    sck.close()

def client_connection(client, connection):
    ip = connection[0]
    port = connection[1]
    
    #print(f"Cliente || (IP): {ip} (PORTA): {port}!")
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'exit':
            break
        reply = f"{ip} --> {msg.decode()}"
        print(f"{ip}:{port} --> {msg.decode()}")
        saveClient(ip,port,msg.decode());
        client.sendall(reply.encode('utf-8'))
             
    print(f"Cliente (IP): {ip} (PORTA): {port}, desconectou-se!")
    client.close()

Server()
