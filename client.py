import socket 
import time;
import argparse
import random;
import PySimpleGUI as sg;
import threading;
import pyrebase;

firebaseConfig = {
    "apiKey": "AIzaSyCK3B0fEzdIZetBdcxGLk5RC2EuKuQIHKU",
    "authDomain": "fodase-d159a.firebaseapp.com",
    "databaseURL": "https://fodase-d159a.firebaseio.com",
    "projectId": "fodase-d159a",
    "storageBucket": "fodase-d159a.appspot.com",
    "messagingSenderId": "1063001470227",
    "appId": "1:1063001470227:web:1f05dde77a907217dd56e6"
  };

firebase = pyrebase.initialize_app(firebaseConfig);

dados = firebase.database();

sg.theme('Dark Blue 3');

WIN_W = 70;
WIN_H = 35;
falha = 0;

layout = [
  [sg.Text(size=(WIN_W,WIN_H),text_color="black",font=("Consolas",15),key="tela")],
  [sg.Input(size=(70,None))],
  [sg.Button(button_text="Enviar",size=(20,1))],
]

parser = argparse.ArgumentParser(description = "Cliente")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 7999)
args = parser.parse_args()
#sg.popup_no_buttons("Conectando ao servidor...",auto_close=True,auto_close_duration=3.0)

window = sg.Window("Chat",layout)


try:
  conexao = socket.create_connection((args.host, args.port));
except Exception as e:
  print(f"Falha na conexão ao servidor!");
  falha = 1;

while( falha != 1 ):  
  m = ""
  event,values = window.read(timeout=10);

  if(event == "Enviar"):
    msg = values[0];
    conexao.sendall(msg.encode('utf-8'));
    data = conexao.recv(1024);

  mensagens = dados.child("mensagens").get();
  for mensagens in mensagens.each():
    m += mensagens.val()+"\n";

  window["tela"].update(m);
  if event == sg.WIN_CLOSED or event == 'Exit':
    conexao.close();
    break;
  

  

