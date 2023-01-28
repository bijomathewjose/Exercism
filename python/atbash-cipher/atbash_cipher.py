T={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}
def encode(plain_text):
    val=''
    count=0
    for i in plain_text:
        if count==5:
            val+=" "
            count=0
        if i.isdigit():
            val+=i
            count+=1
        elif i.isalpha():
            val+=T[i.lower()]
            count+=1
    return val.strip()
    pass

def decode(ciphered_text):
    val=''
    count=0
    for i in ciphered_text:
        if i.isdigit():
            val+=i
            count+=1
        elif i.isalpha():
            val+=T[i.lower()]
            count+=1
    return val.strip()
    pass