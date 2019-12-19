import socket
import Th

#inicia a porta e endereco do servidor
port= 40000
host=''
end=(host,port)
conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(end)
conn.listen(500)
#cria threads para responder cada conexao
while True:
    conex =conn.accept()
    con, cliente= conex
    print("Connect.")
    #inicia a thread que esta no arquivo Th.py
    obj=Th.conex(conex)
    obj.start()
conn.close()