import re


class Parser:
    def __init__(self, file):
        self.file = file

    def parse_grammar(self):
        rules = {}
        with open(self.file, 'r') as fp:
            for line in fp:
                start = re.split(" -> ", line.strip('\n'))[0]
                end = re.split(" -> ", line.strip('\n'))[1]
                rules[start] = [tuple(a.split()) for a in re.split(" \| ", end)]
        return rules




    def parse_grammar_without_pipelines(self):
        rules = {}
        with open(self.file, 'r') as fp:
            for line in fp:
                start = re.split(" -> ", line.strip('\n'))[0]
                end = re.split(" -> ", line.strip('\n'))[1]
                try:
                    rules[start].append(tuple(end.split()))
                except KeyError:
                    rules[start] = []
                    rules[start].append(tuple(end.split()))
        return rules

    def print_rules(rules = {}):
        for key, value in rules.items():
            list = []
            for tuple in value:
                for el in tuple:
                    list.append(el)
                list.append("|")
            #print key, " -> ", " | ".join([str(tuple[i]) for tuple in value for
                #  i in range(len(tuple))])
            print key, " -> ", " ".join(list[:-1])


if __name__ == '__main__':
    parser = Parser('grammar_new')
    #rules = parse_grammar('grammar.txt')
    #print_rules(rules)
    rules = parser.parse_grammar_without_pipelines()
    print rules

