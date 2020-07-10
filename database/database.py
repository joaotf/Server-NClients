import Pyro4;

def saveKey(uri):
  with open("../config/key.txt","w+") as file:
    file.write(str(uri));
  file.close()

@Pyro4.expose
class Chat:
  def adicionaClients(self,ip,port,mensagem):
    with open("../utils/log.txt","a+") as f:
      f.write(str(ip)+":"+str(port)+" >> "+mensagem+"\n");
    f.close();

daemon = Pyro4.Daemon();

uri = daemon.register(Chat);

saveKey(uri);

daemon.requestLoop()

