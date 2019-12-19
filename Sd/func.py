import socket
import Dados
#Client part
host='localhost'
port=40000
end=(host,port)

def Publisher(msg):
    conn= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(end)
    conn.send("0")
    hab=conn.recv(100)
    print(msg)
    conn.send(msg)
    conn.close()

def Subscriber(id):
    conn= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(end)
    conn.send("1")
    msg=conn.recv(1024)
    conn.send(str(id))
    msg=conn.recv(1024)
    conn.close()
    return msg

def SubscribeAct(id, op, val):
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect(end)
    conn.send("2")
    msg=conn.recv(1024)
    #no agressive deve se usar o IP no lugar de local host
    msg=(id+";"+op+";"+val+";"+"localhost")
    conn.send(msg)
    msg=conn.recv(1024)
    print(msg)
    conn.close()
