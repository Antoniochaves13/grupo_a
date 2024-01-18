from Classe_Endereco import Endereco
import time
import os
"""def limpa_tela():
    sistema_operacional = os.name
    if sistema_operacional == "posix":
        os.system("clear")
    elif sistema_operacional == "nt":"""

class Agenda():
    def __init__(self,nome,numero,email,cod_post,endereco):
        self.nome=nome
        self.numero=numero
        self.email=email
        self.cod_post=cod_post
        self.endereco = endereco
        self.n = 1
        self.t = 2
        self.ender = []

    def adicionar(self):
        while self.n != 0:
              print("")
              print("***OUTRO CONTACTO A SER CADASTRADO...***")
              print("")
              nome1 = input("Insira o nome para adicionar aos contactos: ")
              print("Nome<",nome1,">adicionado!")
              numero1 = int(input("Insira o número de telefone para adicionar aos contactos: "))
              print("Telefone<", numero1, ">adicionado!")
              email1 = input("Insira o email para adicionar aos contactos: ")
              print("Email<", email1, ">adicionado!")
              cod_post1 = input("Insira o código postal para adicionar aos contactos: ")
              print("codigo_postal<", cod_post1, ">adicionado!")
              rua1 = input("Insira a rua para adicionar ao endereço: ")
              casa1 = input("Insira a casa para adicionar ao endereço: ")
              municipio1 = input("Insira o município para adicionar ao endereco: ")
              provincia1 = input("Insira a província para adicionar ao endereço: ")
              pais1 = input("Insira o país para adicionar ao endereço: ")
              id = input("F para pessoa física, J para pessoa jurídica: ")
              if id == "F":
                  bi1 = input("Insira o BI para adicionar ao endereço: ")
                  contatos[nome1] = numero1, email1, cod_post1, "Endereço:", rua1, casa1, municipio1, provincia1, pais1, bi1
              elif id == "J":
                  nif1 = input("Insira o NIF para adicionar ao endereço: ")
                  contatos[nome1] = numero1, email1, cod_post1, "Endereço:", rua1, casa1, municipio1, provincia1, pais1, nif1
              else:
                  print("Opção inválida!")
              print(f"Contato <{nome1}> adicionado com sucesso.")
              print("")
              print("DESEJA CONTINUAR A ADICIONAR CONTACTOS? DIGITE [0]NÃO/[1]SIM")
              self.n = int(input("Digite o número para escolher a opção: "))
              print("")

    def editar(self):
        while self.t != 1:
              nome1 = input("Insira o nome para editar: ")
              if nome1 in contatos:
                 print("Nome<", nome1, ">encontrado! É possível editar.")
                 print("")
                 novo_numero = int(input("Insira o novo número de telefone para editar: "))
                 print("Número novo<",  novo_numero, ">adicionado!")
                 novo_email = input("Insira o novo email para editar: ")
                 print("Email novo<", novo_email, ">adicionado!")
                 novo_cod_post = input("Insira o código postal para editar: ")
                 print("codigo_postal novo<", novo_cod_post, ">adicionado!")
                 nova_rua = input("Insira a nova rua para editar: ")
                 print("Rua nova<", nova_rua, ">adicionada")
                 nova_casa = input("Insira a nova casa para editar: ")
                 print("Casa nova<", nova_casa, ">adicionada")
                 novo_municipio = input("Insira o novo município  para editar: ")
                 print("Município novo<", novo_municipio, ">adicionado")
                 nova_provincia = input("Insira a nova província para editar: ")
                 print("Provincía nova<", nova_provincia, ">adicionada")
                 novo_pais = input("Insira o novo país para editar: ")
                 print("País novo<", novo_pais, ">adicionado")
                 id = input("F para pessoa física, J para pessoa jurídica: ")
                 if id == "F":
                    novo_bi = input("Insira o BI novo para adicionar ao endereço: ")
                    print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_bi}")
                    print("BI novo<",novo_bi,">adicionado")
                 elif id == "J":
                     novo_nif = input("Insira o NIF para adicionar ao endereço: ")
                     print(f"Endereço de <{nome1}> atualizado para {nova_rua, nova_casa, novo_municipio, nova_provincia, novo_pais, novo_nif}")
                     print("NIF novo<", novo_nif, ">adicionado")
                 else:
                     print("Opção inválida!")
                 print("")
                 print("DESEJA CONTINUAR A EDITAR? DIGITE [1]NÃO / [2]SIM")
                 self.t = int(input("Digite o número para escolher a opção: "))
                 print("")
                 print(contatos)
                 print("")
                 contatos[nome1] = novo_numero,novo_email,novo_cod_post
                 print(f"Número de <{nome1}> atualizado para {novo_numero}.")
                 print(f"Email de <{nome1}> atualizado para {novo_email}.")
                 print(f"Código Postal de <{nome1}> atualizado para {novo_cod_post}.")
                 print("")
              else:
                  print(f"Contato <{nome1}> não encontrado, não pode ser editado. Insira novamente...")

    def remover(self):
        nome1 = input("Insira o novo nome para remover: ")
        print("Nome<", nome1, ">encontrado! É possível remover.")
        if nome1 in contatos and nome1 == self.nome or self.nome in contatos:
            del contatos[nome1]
            print(f"Contato <{nome1}> removido.")
            print("")
        else:
            print(f"Contato <{nome1}> não encontrado, não pode ser removido.")

    def pesquisar(self):
        nome1 = input("Insira o nome para pesquisar:")
        if nome1 in contatos:
            print(f"Contato <{nome1}> encontrado.")
            print("")
        else:
            print(f"Contato <{nome1}> não encontrado, fim da pesquisa.")
            print(contatos[nome1])
            print("")

    def listar(self):
        for self.nome1,self.numero1 in contatos.items():
            #for nome, email in self.contatos.items():
                   print(f"{self.nome1}: {self.numero1}")
                   print("")

    def adicionar1(self): #Método para a instanciação
        contatos[self.nome] = self.numero, self.email, self.cod_post, "Endereço:",elemento.endereco.rua,elemento.endereco.casa,elemento.endereco.municipio,elemento.endereco.provincia,elemento.endereco.pais,elemento.endereco.bi
        print(f"Contato <{self.nome}> adicionado com sucesso.")
        print("")


Contactos = []
ende=Endereco("Rua-1","Casa-1","Cacuaco","Luanda","Angola","012LA","013LA")
agenda=Agenda("Gilson",1234,"gil@gmail.com","+2441234",ende)
Contactos.append(agenda)

ende=Endereco("Rua-2","Casa-2","Viana","Luanda","Angola","014LA","015LA")
agenda=Agenda("Maria",1234,"maria@gmail.com","+2441234",ende)
Contactos.append(agenda)

print("")
print("«««««««««««««««««««««««««««««««««««« BEM VINDO À NOSSA AGENDA TELEFÓNICA »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
print("Tu podes adicionar,editar,remover,pesquisar ou listar os contactos cadastrados.\nINICIALIZANDO EM 2 SEGUNDOS...")
time.sleep(2)
print("")

for elemento in Contactos:
    
    print("============================================= Adicionando: ================================================")
    elemento.adicionar1()
    print("Nome:",elemento.nome)
    print("Número:",elemento.numero)
    print("Email:",elemento.email)
    print("Código postal:",elemento.cod_post)
    print("Endereço: (",elemento.endereco.rua,",",elemento.endereco.casa,",",elemento.endereco.municipio,",",elemento.endereco.provincia,",",elemento.endereco.pais,",",elemento.endereco.bi,")")
    print("")
    print("===========================================================================================================")
    #os.system("cls")
print("============================================== MENU PRINCIPAL =================================================")
print("")
opcao = 0

while opcao != 6:
      print("1-Adicionar contactos")
      print("2-Editar contactos")
      print("3-Remover contactos")
      print("4-Listar contactos")
      print("5-Pesquisar contactos")
      print("6-Sair")
      print("")
      print("=========================================================================================================")
      print("")
      opcao = int(input("Escolha um número para a opção desejada: "))
      if opcao == 1:
          print("======================================== Adicionando: ===============================================")
          agenda.adicionar()
          print("*****************************************************************************************************")
      elif opcao == 2:
          print("========================================== Editando: ================================================")
          agenda.editar()
      elif opcao == 3:
          print("========================================== Removendo: ===============================================")
          agenda.remover()
          print("*****************************************************************************************************")
      elif opcao == 4:
          print("========================================== Listando: ================================================")
          agenda.listar()
          print("*****************************************************************************************************")
      elif opcao == 5:
          print("========================================== Pesquisando: =============================================")
          agenda.pesquisar()
          print("*****************************************************************************************************")
      elif opcao == 6:
          print("O SISTEMA VAI ENCERRAR EM 2 SEGUNDOS...!")
          time.sleep(2)
          print("ENCERRADO COM ÊXITO!!")
          print("*****************************************************************************************************")

 
