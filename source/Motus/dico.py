import random

class Dico:

  def __init__(self, path):

    self.file = open(path / 'dico.txt', 'r')
    self.content = self.file.read()

    self.list_word = self.content.split('\n')
    self.nb_word = len(self.list_word)

  def random_word(self, lenght):

    word = ''

    while len(word) != lenght:
        word = self.list_word[random.randint(0, self.nb_word)]
      
    return word

  def in_dico(self, word):

  	return word in self.list_word