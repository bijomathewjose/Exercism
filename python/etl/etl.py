def transform(legacy_data):
    new_legacy_data = { letter.lower(): int(number) for number in legacy_data for letter in legacy_data[number] }
    letters = sorted([j.lower() for i in legacy_data.values() for j in i])
    return {letter: new_legacy_data[letter] for letter in letters}
    pass
