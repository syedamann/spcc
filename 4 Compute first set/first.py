def readRules(f):
    with open(f) as t:
        rules = []
        for line in t:
            rules.append(line.replace(" ","").strip().split('\n'))

    return rules

# Considering Lowercase Letter are Terminal & Uppercase Letter Non-Terminal

def create_Firsts(rules):
    firsts = []
    dict = {}
    firsts_dict = {}
    firsts.append([sublist[0][0] for sublist in rules])

    var = []
    temp_list = []
    for i in range(len(firsts[0])):
        var.append(firsts[0][i])
        temp_list = getFirsts(var[i], rules)
        dict[var[i]] = temp_list
        
    for i in range(len(firsts[0])):
        temp_list = dict[var[i]]
        temp_list = FirstsRule3(var[i], rules, temp_list, firsts[0], dict)
        firsts_dict[var[i]] = temp_list
    
    return firsts_dict, firsts

def getFirsts(var, rules):
    firsts_func = []
    for x in range(len(rules)):
        if (var == rules[x][0][0]):
            # RULE 1
            char = rules[x][0][3]
            if char.islower():
                firsts_func.append(char)

            # RULE 2
            if (rules[x][0].find('E') != -1):
                firsts_func.append('E')
    return firsts_func

def FirstsRule3(var, rules, temp_list, firsts, dict):
    lst = []
    for x in range(len(rules)):
        if (var == rules[x][0][0]):
            # RULE 3
            char = rules[x][0][3]
            if char in firsts:
                for i in range(len(rules)):
                    if (char == rules[i][0][0]):
                        lst = dict[char]
                        temp_list.extend(lst)
    return temp_list

f = '4 Compute first set\input.txt'
rules = readRules(f)
firsts_dict, terminal_var_list = create_Firsts(rules)
print("First Function Values:")
for i in range(len(terminal_var_list[0])):
    x = terminal_var_list[0][i]
    print ('first({})'.format(x), "=", firsts_dict[x])


print()