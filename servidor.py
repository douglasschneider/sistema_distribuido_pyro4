import Pyro4
import os.path

@Pyro4.expose
class GreetingMaker:
    def Arquivo(self, arquivolido):
        resultado = os.path.exists(arquivolido)
        return resultado

daemon = Pyro4.Daemon()                         # Servidor instância o Objeto remoto
uri = daemon.register(GreetingMaker)            # Servidor registra e vincula o objeto em uma porta

ns = Pyro4.locateNS()
ns.register('dem', uri)

print('Programa Rodando')
daemon.requestLoop()
