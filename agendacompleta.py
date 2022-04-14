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

#para função para execusão das query: insert/delete/update
def query(conexao,sql):

    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("operação realizada com sucesso")
        conexao.close()

#select
def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall() #resultado da pesquisa
    return res



def menuPrincipan():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registros Nomes")
    print("6 - Sair")

def menuinserir():
    os.system("cls")
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vmail=input("Digite o e-mail:")

    vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TEEFONECONTATO,T_EMAILCONTATO) VALUES('"+vnome+"','"+vtelefone+"','"+vmail+"')"
    query(vcon,vsql)
    os.system("pause")



def menudeletar():
    os.system("cls")
    vid=input("Digite o id do registro a ser deletado: ")

    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=)"+vid
    query(vcon,vsql)
    os.system("pause")

def menuAtualizar():
    os.system("cls")
    vid=input("Digite o id do registro a ser alterado: ")
    r=consultar(vcon,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input("Digite o nome: ")
    vtelefone=input("Digite o telefone: ")
    vemail=input("Digite o e-mail:")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"',T_TEEFONECONTATO='"+vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)
    os.system("pause")

def menuConsultar():
    vsql="SELECT * FROM tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} TELEFONE:{2:_<14} EMAIL:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
    os.system("pause")
    os.system("cls")
    print("Fim da lista")
    os.system("pause")

def menuConsultarNomes():
    vnome=input("Digite o nome:")
    vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} TELEFONE:{2:_<14} EMAIL:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
    os.system("pause")
    os.system("cls")
    print("Fim da lista")
    os.system("pause")



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
        menuConsultar()
    elif opc==5:
        menuConsultarNomes()
    elif opc==6:
        os.system("cls")
        print("programa finalizado")
    else:
        os.system("cls")
        print("opção invalida")
        os.system("pause")

vcon.close()
os.system("pause")

        