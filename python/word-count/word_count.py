def count_words(sentence):
    sentence=sentence.lower()
    clean_sentence=deal_with_unwanted_sym(sentence)
    word_list=clean_sentence.split()
    new_word_list=find_word_with_quotes(word_list)
    return {i:new_word_list.count(i) for i in new_word_list}
    pass
def deal_with_unwanted_sym(sentence):
    for i in sentence:
        if not(i.isalnum() or i in '\''):
            sentence=sentence.replace(i,' ')
    return sentence
def deal_with_quotes(word):
    word=word.strip("'")
    return word
    pass
def find_word_with_quotes(word_list):
    for index,word in enumerate(word_list):
        if "'" in word:
            word_new=deal_with_quotes(word)
            if word_new=='':
                word_list.remove(word)
            else:
                word_list[index]=word_new
    return word_list
    pass