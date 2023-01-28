def find_anagrams(word, candidates):
    anagrams = []
    word=word.lower()
    for candidate in candidates:
        candidate_low=candidate.lower()
        if candidate_low == word:
            continue
        candidate_is_anagram = True
        for letter in candidate_low:
            if word.count(letter) != candidate_low.count(letter) or letter not in word:
                candidate_is_anagram = False
        if candidate_is_anagram:
            anagrams.append(candidate)
    return anagrams
    pass