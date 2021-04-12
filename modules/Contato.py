class Contato:
  def __init__(self, nome, telefone, endereco, relacao):       #Inicializador da classe
    self.__nome = nome
    self.__telefone = telefone
    self.__endereco = endereco
    self.__relacao = relacao

  @property
  def nome(self):                                              #Getter do nome
    return self.__nome

  def __str__(self):                                           #Método toString()
    return f'{self.__nome} - {self.__telefone} - {self.__endereco} - {self.__relacao}'
