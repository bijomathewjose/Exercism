def translate(text):
    words=text.split()
    word=[]
    for i in words:
        word.append(translate_word(i))
    return " ".join(word);
def translate_word(text):
    vowel_sound=['a','e','i','o','u','xr','yt']
    for i in vowel_sound:
        if i==text[0] or i==text[0:2]:
            return text+"ay"
    vowel_sound=['a','e','i','o','u']
    if "qu" in text:
        index=text.find('qu')
        return text[index+2:]+text[:index+2]+"ay"
    if 'y' in text[1:len(text)-2] or len(text)==2:
        return compute_word('y',text) 
    for i in text:
        if i in vowel_sound:
            return compute_word(i,text)

def compute_word(characters,text):
    index=text.find(characters)
    return text[index:]+text[:index]+"ay"
    