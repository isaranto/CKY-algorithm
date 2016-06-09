import re


class Rule_p:
    def __init__(self, line):
        """
        Rule is being parsed like this: eg. "S -> NP VP" will become an object Rule with non-terminal = S,
        first = NP and second VP
        :param line:
        :return:
        """
        start = re.split(" -> ", line.strip('\n'))[0]
        end = re.split(" -> ", line.strip('\n'))[1]
        self.non_terminal = start
        if len(end.split()) == 2:
            self.terminal = False
            self.first = end.split()[0]
            self.second = end.split()[1]
        elif len(end.split()) == 1:
            self.terminal = True
            self.word = end.split()[0]

    def print_me(self):
        if self.terminal:
            print self.non_terminal, " -> ", self.word
        else:
            print self.non_terminal, " -> ", self.first, self.second


class Grammar_p:
    def __init__(self, file):
        """
        Rules are being parsed into a dictionary of [first, second] = non_terminal
        :param file:
        :return:
        """
        _dict = {}
        vocab = {}
        with open(file, 'r') as fp:
            for line in fp:
                rule = Rule(line)
                if rule.terminal:
                    vocab[rule.word] = rule.non_terminal
                else:
                    _dict[rule.first, rule.second] = rule.non_terminal
        self.rules = _dict
        self.vocab = vocab

    def print_me(self):
        print "Grammar Rules"
        for key, value in self.rules.items():
            tmp = Rule_p(str(value)+" -> "+str(key))
            tmp.print_me()
        print "\nVocabulary :"
        for key, value in self.vocab.items():
            print value, " -> ", key


if __name__ == '__main__':
    _file = 'grammar_new'
    grammar = Grammar_p(_file)
    rules = grammar.rules
    grammar.print_me()
    print grammar.rules
