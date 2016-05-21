import re


def parse_grammar(file):
    rules = {}
    with open(file, 'r') as fp:
        for line in fp:
            list = []
            start = re.split(" -> ", line.strip('\n'))[0]
            end = re.split(" -> ", line.strip('\n'))[1]
            rules[start] = [tuple(a.split()) for a in re.split(" \| ", end)]
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
    rules = parse_grammar('grammar.txt')
    print_rules(rules)
