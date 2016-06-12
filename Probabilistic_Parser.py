import re


class Rule_p:
    def __init__(self, line):
        """
        Rule is being parsed like this: eg. "S -> NP VP [0.5]" will become an object Rule with non-terminal = S,
        first = NP, second = VP and prob = 0.5
        :param line:
        :return:
        """
        start = re.split(" -> ", line.strip('\n'))[0]
        end = re.split(" -> ", line.strip('\n'))[1]
        # re.findall("\d.\d+",a)
        self.non_terminal = start
        if len(end.split()) == 3:
            self.terminal = False
            self.prob = float(re.findall("\d.\d+|\d+", end)[0])
            self.first = end.split()[0]
            self.second = end.split()[1]
        elif len(end.split()) == 2:
            self.terminal = True
            self.prob = float(re.findall("\d.\d+|\d+", end)[0])
            self.word = end.split()[0]

    def print_me(self):
        if self.terminal:
            print self.non_terminal, " -> ", self.word, "[", self.prob, "]"
        else:
            print self.non_terminal, " -> ", self.first, self.second,  "[", self.prob, "]"


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
                rule = Rule_p(line)
                if rule.terminal:
                    vocab[rule.word] = (rule.non_terminal, rule.prob)
                else:
                    _dict[rule.first, rule.second] = (rule.non_terminal, rule.prob)
        self.rules = _dict
        self.vocab = vocab

    def print_me(self):
        print "Grammar Rules"
        for key, value in self.rules.items():
            try:
                print value[0]," -> ", key, "[", value[1] ,"]"
                #tmp = Rule_p(str(value)+" -> "+str(key))
                #tmp.print_me()
            except:
                pass
        print "\nVocabulary :"
        for key, value in self.vocab.items():
            print value[0]," -> ", key, "[", value[1] ,"]"


if __name__ == '__main__':
    _file = 'probabilistic_grammar'
    grammar = Grammar_p(_file)
    rules = grammar.rules
    grammar.print_me()
    # print grammar.rules
