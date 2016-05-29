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
                # self.matrix[i, j] = None if j <= i else []
                self.matrix[i, j] = [None]
                try:
                    if j-i == 1:
                        self.matrix[i, j].append(self.vocab[sentence.split()[j-1]])
                        del self.matrix[i, j][0]
                except KeyError:
                    pass

    def print_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                for item in self.matrix[i, j]:
                    print str(item).ljust(15),
            print ""

    def run_cky(self):
        print "Running CKY algorithm"
        for j in range(self.cols):
            counter = j-1  # access only above diagonal of matrix
            for i in range(counter-1, -1, -1):
                #ones = self.matrix[i, j-1]
                lefts = next(self.matrix[i, col] for col in range(j, 0, -1) if any(x is not None for x in
                                                                                   self.matrix[i, col]))
                downs = next(self.matrix[row, j] for row in range(i, self.rows) if any(x is not None for x in
                                                                                       self.matrix[row, j]))
                #ones = next(self.matrix[i, k] for k in range(j, counter, -1) if not self.matrix[i, k])
                if lefts and downs:
                    for left in lefts:
                        for down in downs:
                            try:
                                self.matrix[i, j] = [self.rules[left, down]]
                            except:
                                #self.matrix[i, j] = None
                                pass


if __name__ == '__main__':
    _file = 'grammar_new'
    grammar = Parser.Grammar(_file)
    rules = grammar.rules
    grammar.print_me()
    _sentence = "I saw the doctor with the white shirt"
    cky = Cky(_sentence, grammar)
    cky.run_cky()
    #print rules
    cky.print_matrix()

