import string
def is_pangram(sentence):
    letters=string.ascii_lowercase
    for letter in letters:
        if letter not in sentence.lower():
            return False
    return True
    pass
