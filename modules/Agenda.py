class Agenda:
  def __init__(self):                                          #Inicializador da classe
    self.__contato = []
  
  def buscar(self,nome_do_item):                                    #Busca e retorna um contato caso ele exista
    for i in range(len(self.__contato)):
      if nome_do_item in self.__contato[i].nome:
        print("Contato encontrado!")
        return self.__contato[i]
    return -1

  def __busca_indice(self,nome_do_item):                            #Busca um contato e retorna o seu indice dentro do vetor
    for i in range(len(self.__contato)):
      if nome_do_item in self.__contato[i].nome:
        return i
    return -1

  def inserir(self, item):                                     #Insere um contato no fim da lista
    size = len(self.__contato)
    if size == None or size <= 1000:
      if self.__busca_indice(item.nome) == -1:
        self.__contato.append(item)
        print("Contato inserido com sucesso!")
      else:
        print("O contato já existe e sera alterado")
        self.alterar(item)
    else:
      print("A agenda esta cheia, delete algum contato para abrir espaco!")

  def alterar(self, item):                                     #Altera as informações de um contato de mesmo nome do contato passado
    alterado = self.__busca_indice(item.nome)
    if alterado == -1:
      print("Contato não encontrado!")
    else:
      self.__contato[alterado] = item
      print("Contato alterado com sucesso!")

  def remover(self, nome_do_item):                                     #Busca o indice do contato e o remove
    idx = self.__busca_indice(nome_do_item)
    self.__contato.pop(idx)

  def listar(self):                                            #Lista todos os contatos da agenda
    print('-'*50 ,'\n')
    for item in self.__contato:
      print(item)
    print('-'*50)