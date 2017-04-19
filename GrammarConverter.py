# Global dictionary used for storing the rules.
RULE_DICT = {}


def read_grammar(grammar_file):
    """
    Reads in the given grammar file and splits it into separate lists for each rule.
    :param grammar_file: the grammar file to read in.
    :return: the list of rules.
    """
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]


def add_rule(rule):
    """
    Adds a rule to the dictionary of lists of rules.
    :param rule: the rule to add to the dict.
    """
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])


def convert_grammar(grammar):
    """
        Converts a context-free grammar in the form of

        S -> NP VP
        NP -> Det ADV N

        and so on into a chomsky normal form of that grammar. After the conversion rules have either
        exactly one terminal symbol or exactly two non terminal symbols on its right hand side.

        Therefore some new non terminal symbols might be created. These non terminal symbols are
        named like the symbol they replaced with an appended index.
    :param grammar: the CFG.
    :return: the given grammar converted into CNF.
    """

    # Remove all the productions of the type A -> X B C or A -> B a.
    global RULE_DICT
    unit_productions, result = [], []
    res_append = result.append
    index = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            # Rule is in form A -> X, so back it up for later and continue with the next rule.
            unit_productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            # Rule is in form A -> X B C or A -> X a.
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    # Create a new non terminal symbol and replace the terminal symbol with it.
                    # The non terminal symbol derives the replaced terminal symbol.
                    rule[item[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", item[0]]
                index += 1
            while len(rule) > 3:
                new_rules += [f"{rule[0]}{str(index)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        # Adds the modified or unmodified (in case of A -> x i.e.) rules.
        add_rule(rule)
        res_append(rule)
        if new_rules:
            res_append(new_rules)
    # Handle the unit productions (A -> X)
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE_DICT:
            for item in RULE_DICT[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    res_append(new_rule)
                else:
                    unit_productions.append(new_rule)
                add_rule(new_rule)
    return result
