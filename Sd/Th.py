from threading import Thread
import func
import os
from Dados import fila
from Dados import subscribers
from Dados import concatena
from Dados import replace 
from Dados import PadraoTipo
from Dados import agressiveIP

class conex(Thread):
    def __init__(self,num):
        Thread.__init__(self)
        self.conn, self.client=num




    def run(self):
        global fila
        global concatena
        global replace
        global PadraoTipo
        global subscribers
        global agressiveIP
        #recebe a operacao feita pelo cliente
        op=str(self.conn.recv(100))
        #Parte Publish
        if op=="0":
            self.conn.send("1")
        #recupera a mensagem do publish a atribui ela a uma no solucao
            msg=self.conn.recv(1024)
            end, nmsg, tipo=msg.split(";")
            if tipo =="0":
                if end in fila:
                    tipo="1"
                elif end in concatena:
                        tipo="2"
                elif end in replace:
                    tipo="3"
                else:
                    tipo=PadraoTipo

            if tipo =="1":
                if end not in fila:
                    fila[end]=[]
                fila[end].append(nmsg)
                print(str(end)+":"+str(fila[end]))

            if tipo =="2":
                if end not in concatena:
                    concatena[end]=[]
                concatena[end].append(nmsg)
                print(str(end)+":"+str(concatena[end]))

            if tipo =="3":
                replace[end]=nmsg
                print(str(end)+":"+str(replace[end]))
            self.conn.close()
            #apenas para o funcionamento do agressive
            #agres=agressive(end,msg)
            #agres.start()
        #Parte recebe suas inscricoes



        if op=="1":
            self.conn.send("1")
            id=self.conn.recv(1024)
            msg=""
            try:
                for k in subscribers[id]:
                    try:
                        msg=str(msg)+"\n"+str(k)+": "+str(fila[k][0])    
                        del fila[k][0]
                        msg=str(msg)+"\n"+str(k)+": "+str(replace[k][0])
                        msg=str(msg)+"\n"+str(k)+": "+str(concatena[k])
                    except:
                        print("Erro com id: "+id)

            except:
                msg="nao esta registrado em nenhuma"

            self.conn.send(msg)
            self.conn.close()
       
        #Parte em que voce se inscreve em novos canais
        if op=="2":
            self.conn.send("1")
            msg=self.conn.recv(1024)
            id,op,val,ip=msg.split(";")
            #Inscreve no canal recebido
            if op=="1":
                if id not in subscribers:
                    subscribers[id]=[]
                if val not in subscribers[id]:
                    subscribers[id].append(val)
                print(subscribers[id])
                #agressiveIP[val].append(ip)
                self.conn.send("ok")

                
            #remove um canal
            if op=="2":
                subscribers[id].remove(val)
                self.conn.send("ok")


            #remove a prorpia inscricao
            if op=="3":
                del subscribers[id]
                self.conn.send("ok")


            #envia as inscricoes de um pedido
            if op=="4":
                try:
                    msg=str(subscribers[id])
                except:
                    msg="nao possui inscricao"
                self.conn.send(msg)


            self.conn.close()
            #essa parte e apenas para o funcionamento do agressive
        os.system("clear")
        for k in fila.keys():
            print(str(k)+": "+str(fila[k]))
            
class agressive(Thread):
    def __init__(self, end, msg):
        self.end=end
        self.msg=msg
    def run(self):
        global agressiveIP
        for k in agressiveIP[self.end]:
            try:
                ip=agressiveIP[self.end][k]
                port= 4001
                connend=(ip,port)
                conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn.connect(end)
                conn.send(self.msg)
                conn.close()
            except:
                print(str(agressiveIP[self.end][k])+"nao recebeu")
