def is_paired(input_string):
    if input_string.replace(' ', '') == '':
        return True
    containers = ['[', ']', '{', '}', '(', ')']
    openers = {'[': ']', '{': '}', '(': ')'}
    only_symbols = [i for i in input_string if i in containers]
    open_list = []
    while only_symbols:
        if not only_symbols[0] in openers.keys():
            return False
        open_list+=get_the_open_list(only_symbols,openers)
        if len(only_symbols) == 0 and len(open_list) > 0:
            return False
        open_list,only_symbols = closed_open_list(open_list,only_symbols,openers)
    return True
    
def closed_open_list(open_list,only_symbols,openers):
    while only_symbols:
            if len(open_list)>0 and only_symbols[0]==openers[open_list[-1]]:
                open_list.pop()
                only_symbols.pop(0)
            else:
                break
    return (open_list,only_symbols)
def get_the_open_list(only_symbols,openers):
    open_list=[]
    while only_symbols:
        if only_symbols[0] in openers.keys():
            open_list.append(only_symbols.pop(0))
        else:
            break
    return open_list
    pass

def getIndex(array, start, end, val):
    for i in range(end, start, -1):
        if array[i] == val:
            return i
    return -1