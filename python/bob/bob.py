def response(hey_bob):
    copy=hey_bob.strip()
    if copy.isupper():
        return "Calm down, I know what I'm doing!" if copy.endswith('?') else 'Whoa, chill out!'   
    return 'Sure.' if copy.endswith('?') else "Fine. Be that way!" if copy=="" else "Whatever."