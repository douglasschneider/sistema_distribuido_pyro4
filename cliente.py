import Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('dem')

greeting_maker = Pyro4.Proxy(uri)                   # Acesso remoto do cliente ao servidor

print('Cliente')

resultado_arquivo = greeting_maker.Arquivo('teste.txt')     # Chamada do método

# Apresentar Resultados
if (resultado_arquivo == False):
    print('Arquivo não encontrado')
else:
    print('Arquivo encontrado')
