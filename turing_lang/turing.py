import argparse

# arg parsing, getting the file

def clean_string(string):
    """ Removes whitespace, indentation, and breaks. """
    string = string.replace("\n","")
    string = string.replace("\r","")
    string = string.replace(" ","")
    string = string.replace("\t","")
    return string

def get_rule(tape, rules, state, position):
    """ Returns a rule.

    Rule determined by the given state and position, selected out of
    the given rules list and from the given tape.

    """
    if position > len(tape) - 1:
        tape.append('b')
    if position < 0:
        tape.insert(0, 'b')
        position = 0

    for rule in rules:
        rule_state = rule[0]
        rule_symbol = rule[1]
        current_symbol = tape[position]
        current_state = state

        if (rule_state == current_state):
            if (rule_symbol == current_symbol):
                return rule, position
    return (None, None)

def use_rule(tape, rule, state, position):
    """ Returns a tape after being modified by the given rule. """
    printed = rule[2]
    next_state = rule[3]
    direction = rule[4]

    tape[position] = printed

    state = next_state

    if (direction == 'r'):  position += 1
    if (direction == 'l'):  position -= 1

    return tape, position, state

def compute(tape, rules):
    """ Returns a computed tape after all the rules are applied. """
    halt = False
    accepted = False
    state = "0"
    position = 0

    while (halt==False):
        file, verbose = get_args()
        if verbose:
            print "Tape", tape, "Position:", position, "State", state
        rule, position = get_rule(tape, rules, state, position)
        if (rule != None):
            tape, position, state = use_rule(tape, rule, state, position)
        else:
            halt = True
    if verbose:
        print ""
    if state == "a":
        accepted = True
    return tape, accepted

def remove_blanks(tape):
    """ Removes excess 'b' symbols on a tape after computation. """
    while (tape.count('b') > 0):
        tape.remove('b')
    return tape

def get_args():
    """ Returns the file and verbosity switch from args. """
    parser = argparse.ArgumentParser(description='Compute' +
        'a turing language program')
    parser.add_argument('file',
                        metavar='f',
                        help='file where program is stored',
                        type=str)
    parser.add_argument('--verbose',
                        default=False,
                        help='show steps',
                        action='store_true')

    args = parser.parse_args()
    return args.file, args.verbose

def extract_contents():
    """ Returns the tape and the rules from a file object. """
    tape = None
    rules = []
    file_name, verbose = get_args()
    print file_name
    file = open(file_name, 'r')

    for line in file:
        line = clean_string(line)
        if line != "" and line[0] != "#": # not a comment or blank
            if tape == None: # tape still isn't set
                tape = line.split(",")
            else: # tape is set, looking at rule
                rules.append(line.split(","))

    return tape, rules

def print_rules(rules):
    """ Prints formatted rules. """
    for index, rule in enumerate(rules):
        print "Rule #" + str(index+1) + ": " + str(rule)

def main():
    """ Prints results from computing the given turing program. """
    tape, rules = extract_contents()
    print "Original Tape: " + str(tape)
    print ""
    print_rules(rules)
    print ""
    tape, accepted = compute(tape, rules)
    tape = remove_blanks(tape)

    print "Result tape: " + str(tape)
    if accepted:
        print "(accepted)"
    else:
        print "(not accepted)"

main()
