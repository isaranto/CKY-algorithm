import re


class Rule:
    def __init__(self, line):
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


class Grammar:
    def __init__(self, file):
        _dict = {}
        with open(file, 'r') as fp:
            for line in fp:
                rule = Rule(line)
                try:
                    _dict[rule.non_terminal].append(rule)
                except KeyError:
                    _dict[rule.non_terminal] = []
                    _dict[rule.non_terminal].append(rule)
        self.rules = _dict

    def print_me(self):
        for key, value in self.rules.items():
            for rule in value:
                rule.print_me()



if __name__ == '__main__':
    _file = 'grammar_new'
    grammar = Grammar(_file)
    rules = grammar.rules
    grammar.print_me()
