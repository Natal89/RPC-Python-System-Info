#Client RPC
import time
import info
from xmlrpc.client import ServerProxy # RPC do Python usa HTTP como protocolo de transporte
cliente = ServerProxy('http://localhost:20064', allow_none=True) # criar uma instância cliente localhost e na porta do servidor
# while True:
#     nome = input("Digite o nome para receber o número \n")
#     output = cliente.nome(nome) # chama a função que está implementada do lado do servidor
#     print(output) 

print("Enviando informações do cliente para o servidor...")
time.sleep(2)
resultado = info.system_information()
cliente.info_system(resultado)
print("Fechando cliente...")
