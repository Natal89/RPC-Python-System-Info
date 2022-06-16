# Server RPC
from xmlrpc.server import SimpleXMLRPCServer
# classe que implementa RPC
class RPC:
    # métodos que vamos trabalhar com RPC
    _metodos_rpc = ['info_system',] # 'metodo_x, ' ...
    def __init__(self, direcao): # Construtor
        self._servidor = SimpleXMLRPCServer(direcao, allow_none=True) # instanciar o servidor RPC        
        # registrar os metodos no RPC da lista _metodos_rpc (posso acrescentar mais metodos)
        for metodo in self._metodos_rpc:
            self._servidor.register_function(getattr(self, metodo))

    def info_system(self, info):
        if info:
            print("Informações recebidas do cliente:")
            print(info)
        else:
            print("Informações não recebidas")

    def iniciar_servidor(self): # funcao p iniciar o servidor
        self._servidor.serve_forever()

if __name__ == '__main__' : # função principal
    rpc = RPC(('', 20064)) # o servidor vai ficar escurando no localhost e na porta 20064
    print("Servidor RPC iniciado ... ")
    rpc.iniciar_servidor()