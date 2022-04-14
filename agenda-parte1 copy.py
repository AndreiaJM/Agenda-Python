import os
import sqlite3
from sqlite3 import Error

##Conexão

def conexaoBanco():
    caminho="C:\\Users\\andre\\OneDrive\\Documentos\\cursojs\\Python\\Banco\\agenda_db.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=conexaoBanco()

def menuPrincipan():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def menuConsultarNomes():
    print("deve consultar nomes")

def menuConsultarId():
    print("deve consultar ids")

def menuAtualizar():
    print("deve atualizar")

def menudeletar():
    print("deve deletar")

def menuinserir():
    print("deve inserir")

opcao=0
while(opcao!=6):
    menuPrincipan()
    opc=int(input("Digite ma opção: "))
    if(opc==1):
        menuinserir()
    elif opc==2:
        menudeletar()
    elif opc==3:
        menuAtualizar()
    elif opc==4:
        menuConsultarId()
    elif opc==5:
        menuConsultarNomes()
    elif opc==6:
        os.system("cls")
        print("programa finalizado")
    else:
        os.system("cls")
        print("opção invalida")
        os.system("pause")

os.system("pause")

        