def is_isogram(string):
    lower=string.lower()
    letters=tuple(lower.replace('-','').replace(' ',''))
    for letter in letters:
        if lower.count(letter)>1:
            return False
    return True
    pass
