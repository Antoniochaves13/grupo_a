from Classe_Endereco import Endereco

class Agenda():
    def __init__(self,nome,numero,email,cod_post,endereco):
        self.nome=nome
        self.numero=numero
        self.email=email
        self.cod_post=cod_post
        self.contatos = {}
        self.endereco = endereco

    def adicionar(self):
        self.contatos[self.nome] = self.numero,self.email,self.cod_post
        print(f"Contato <{self.nome}> adicionado com sucesso.")
        print("")

    def editar(self,nome,novo_numero,novo_email,novo_cod_post):
        if nome in self.contatos:
            self.contatos[nome] = novo_numero,novo_email,novo_cod_post
            print(f"Número de <{nome}> atualizado para {novo_numero}.")
            print(f"Email de <{nome}> atualizado para {novo_email}.")
            print(f"Código Postal de <{nome}> atualizado para {novo_cod_post}.")
            print("")
        """else:
            print(f"Contato <{self.nome}> não encontrado.")"""

    def remover(self,nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato <{nome}> removido.")
            print("")
        """ else:
            print(f"Contato <{self.nome}> não enconntrado.")"""

    def pesquisar(self,nome):
        if nome in self.contatos:
            print(f"Contato <{nome}> encontrado.")
            print("")
        else:
            print(f"Contato <{nome}> não encontrado.")

    def listar(self):
        for self.nome,self.numero in self.contatos.items():
            #for nome, email in self.contatos.items():
                   print(f"{self.nome}: {self.numero}")

Contactos = []
ende=Endereco("Rua-1","Casa-1","Cacuaco","Luanda","Angola","012LA","013LA")
agenda=Agenda("jo",1234,"jo@gmail.com","+2441234",ende)
Contactos.append(agenda)

ende=Endereco("Rua-2","Casa-2","Viana","Luanda","Angola","014LA","015LA")
agenda=Agenda("gil",1234,"gil@gmail.com","+2441234",ende)
Contactos.append(agenda)

print("«««««««««««««««« BEM VINDO À NOSSA AGENDA TELEFÓNICA »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
print("***Tu podes adicionar, editar, remover, pesquisar ou listar os contactos cadastrados.****\n***Iniciando...**")
print("")

for elemento in Contactos:

    print("==================== Adicionando:==========================")
    elemento.adicionar()
    print("==================== Listando: ============================")
    elemento.listar()
    print(elemento.endereco.rua)
    print("")
    print("==================== Editando: ============================")
    elemento.editar("jo",4321,"job@gmail.com","+2444321")
    elemento.editar("gil", 5678, "gi@gmail.com", "+2448765")
    print("==================== Listando: ============================")
    elemento.listar()
    print(elemento.endereco.rua)
    print("")
    print("==================== Removendo: ===========================")
    elemento.remover("jo")
    elemento.listar()
    print("==================== Pesquisando: =========================")
    elemento.pesquisar("jo")
    elemento.listar()
    print("")
    print("**OUTRO CONTACTO A SER CADASTRADO...**")
    print("===========================================================================================================")
    print("")