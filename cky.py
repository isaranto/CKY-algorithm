import numpy as np
import Parser
import pprint


class Cky:
    def __init__(self, sentence, grm):
        self.rows = len(sentence.split())
        self.cols = len(sentence.split())+1
        self.rules = grm.rules
        self.vocab = grm.vocab
        self.matrix = {}
        for j in range(self.cols):
            for i in range(self.rows-1, -1, -1):
                self.matrix[i, j] = None if j <= i else []
                try:
                    if j-i == 1:
                        self.matrix[i, j].append(self.vocab[sentence.split()[j-1]])
                except KeyError:
                    pass
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(self.matrix)

    def run_cky(self):
        print "Running CKY algorithm"
        for j in range(1, self.cols):
            counter = j-1  #access only above diagonal of matrix
            for i in range(counter-1, -1, -1):
                one = self.matrix[i, j-1]
                two = self.matrix[i+1, j]
                if one and two:
                    self.matrix[i, j] = self.rules[(one, two)]
                else:
                    self.matrix[i, j] = None






if __name__ == '__main__':
    _file = 'grammar_new'
    grammar = Parser.Grammar(_file)
    rules = grammar.rules
    grammar.print_me()
    _sentence = "I saw the doctor with the white shirt"
    cky = Cky(_sentence, grammar)
    cky.run_cky()

