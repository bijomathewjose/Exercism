from random import randint
def private_key(p):
    return randint(2,p-1)

def public_key(p, g, private):
    return (g**private)%p

def secret(p, public, private):
    return (public**private)%p

