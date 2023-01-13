#Tree ADT

def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list[branches]

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return true

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    print(' '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

def copy_tree(t):
    return tree(label(t), [copy_tree(b) for b in branches(t)]

# some apply
# maybe some syntax wrong
#def add_trees(t1,t2):
#    if is_leaf(t1):
#        return tree(label(t1)+label(t2), branches(t2))
#    elif is_leaf(t2):
#        return tree(label(t1)+label(t2), branches(t1))
#    else:
#        fewer_branch_t, more_branch_t = sorted([branches(t1),branches(t2)],key=len)
#        pad_t1 = fewer_branch_t + [tree(0) for i in range(len(more_branch_t) - len(fewer_branch_t))]
#        pad_t2 = more_branch_t
#        return tree(label(t1)+label(t2),[add_trees(b1,b2) for b1,b2 in zip(pad_t1,pad_t2)])
def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev] += [word]

        prev = word
    return table 
    
def construct_sent(word,table):
    import random
    result = ''
    while word not in ['.','!','?']:
        result += ' '
        result += word
        word = random.choice(table[word])
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt',url='http://composingprograms.com/shakespeare.txt'):
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt',encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.'], table)

