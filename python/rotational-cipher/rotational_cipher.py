def rotate(text, key):
    alpha=list('abcdefghijklmnopqrstuvwxyz')
    key_alpha={i:j for i,j in zip(alpha,[*alpha[key:],*alpha[:key]])}
    return ("").join([i if not i.isalpha() else key_alpha[i] if i.islower() else (key_alpha[i.lower()]).upper() for i in text])
    pass
