import func
import os

id=raw_input("insira o login: ")
choice=0
while choice !="4":
    os.system('clear')
    print("Que tipo de operacao:")
    print("1.publicar")
    print("2.receber as informacoes")
    print("3.inscrever-se")
    print("4.sair")
    print("=========================")
    choice=raw_input("> ")


    if choice=="1":
        os.system('clear')
        canal=raw_input("insira o canal no qual voce deseja publicar:")
        msg=raw_input("insira a mensagem que deseja publicar:")
        pck=(canal+";"+msg+";0")
        func.Publisher(str(pck))



    if choice=="2":
        os.system('clear')
        msg=func.Subscriber(id)
        print(msg)
        raw_input("Pressione enter para continuar...")



    if choice=="3":
        os.system('clear')
        print("Qual operacao deseja realizar:")
        print("1.adicionar")
        print("2.remover")
        print("3.remover todos")
        print("4.recebe os canais inscrito")
        op=str(raw_input())
        if (op=="1") or (op=="2"):
            val=raw_input("valor para realizacao da operacao: ")
            func.SubscribeAct(id,op,val)
        else:
            val="x"
            func.SubscribeAct(id,op,val)
        raw_input("Pressione enter para continuar...")