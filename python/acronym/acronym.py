def abbreviate(words):
    alpha='abcdefghijklmnopqrstuvwxyz\''
    alpha+=' '+alpha.upper()
    for i in words:
        if i not in alpha:
            words=words.replace(i,' ')
    return (''.join([i[0] for i in words.split()])).upper()
    pass
