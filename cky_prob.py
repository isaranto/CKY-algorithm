import Probabilistic_Parser
import sys


class Cky_prob:
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
        print "\n"

    def run_cky(self):
        print "Running CKY algorithm..."
        for j in range(self.cols):
            counter = j-1  # access only above diagonal of matrix
            for i in range(counter-1, -1, -1):
                # ones = self.matrix[i, j-1]
                lefts = next(self.matrix[i, col] for col in range(j, 0, -1) if any(x is not None for x in
                                                                                       self.matrix[i, col]))
                downs = next(self.matrix[row, j] for row in range(i, self.rows) if any(x is not None for x in
                                                                                           self.matrix[row, j]))
                # ones = next(self.matrix[i, k] for k in range(j, counter, -1) if not self.matrix[i, k])
                if lefts and downs:
                    for left in lefts:
                        for down in downs:
                            try:
                                self.matrix[i, j] = [(self.rules[left[0], down[0]][0], left[1]*down[1])]
                            except KeyError:
                                # self.matrix[i, j] = left[0], down[0]None
                                pass
        if 'S' in self.matrix[0, self.cols-1]:
            print "The Sentence belongs to the grammar\n"
        else:
            print "The Sentence does not belong to the grammar\n"

    def level_tree(self, level, row, col):
        try:
            lefts = next(self.matrix[row, x] for x in range(col-1, 0, -1) if any(y is not None for y in
                                                                                   self.matrix[row, x]))
            downs = next(self.matrix[x, col] for x in range(row+1, self.rows) if any(y is not None for y in
                                                                                       self.matrix[row, col]))
            if lefts and downs:
                print "\t"*level, "\t"*level, self.matrix[row, col]
                print "\t"*level, "left branch:", lefts, "right branch:", downs
        except StopIteration:
            pass

    def print_tree(self):
        level = 0
        for j in range(self.cols-1, 0, -1):
            for i in range(0, self.rows):
                self.level_tree(level, i, j)
                level += 1


if __name__ == '__main__':
    _file = 'probabilistic_grammar'
    grammar = Probabilistic_Parser.Grammar_p(_file)
    rules = grammar.rules
    # grammar.print_me()
    _sentence1 = "I saw the doctor with the white shirt"
    _sentence2 = "I met the doctor with the funny look"
    cky = Cky_prob(_sentence1, grammar)
    cky.run_cky()
    cky.print_matrix()
    cky.print_tree()
