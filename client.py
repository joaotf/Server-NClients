import socket 
import time;
import argparse
import random;
import threading;

parser = argparse.ArgumentParser(description = "Cliente")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 7999)
args = parser.parse_args()

falha = 0;

try:
  conexao = socket.create_connection((args.host, args.port));
  while(True):
    msg = input("msg >> ")
    conexao.sendall(msg.encode('utf-8') );
    data = conexao.recv(1024);
except Exception as e:
  print(f"Falha na conexão ao servidor!");
  falha = 1;



  

