#Client RPC
import time
import info
from xmlrpc.client import ServerProxy # RPC do Python usa HTTP como protocolo de transporte
cliente = ServerProxy('http://localhost:20064', allow_none=True) # criar uma instância cliente localhost e na porta do servidor 

print("Enviando informações do cliente para o servidor...")
time.sleep(2)
resultado = info.system_information()
cliente.info_system(resultado)
print("Fechando cliente...")
