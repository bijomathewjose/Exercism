def flatten(iterable):
    flattened=[]
    for piece in iterable:
        if type(piece) == int:
            flattened.append(piece)
        elif type(piece)==str:
            continue
        elif type(piece)==list:
            flattened += flatten(piece)
    return flattened
    pass
