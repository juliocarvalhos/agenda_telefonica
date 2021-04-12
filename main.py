from modules.Agenda import *
from modules.Contato import *

def main():
  lista_de_contatos = Agenda()
  lista_de_contatos.inserir(Contato('Carlos Bazilio',999999999,'Rua A','Professor'))
  lista_de_contatos.inserir(Contato('Julio Carvalho',888888888,'Rua B','Aluno'))
  lista_de_contatos.inserir(Contato('João Victor',777777777,'Rua C','Aluno'))
  lista_de_contatos.inserir(Contato('Carlos Bazilio',666666666,'Rua D','Professor'))
  lista_de_contatos.remover('João')
  lista_de_contatos.listar()

if __name__ == "__main__":
  main()