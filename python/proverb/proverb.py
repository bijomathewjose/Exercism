def proverb(*args,qualifier=None):
    length=len(args)
    sentence=[]
    count=0
    qualifier="" if qualifier==None else str(qualifier)+" "
    while count<length:
        if count<length-1:
            sentence.append("For want of a "+args[count]+" the "+args[count+1]+" was lost.")
        else:
            sentence.append("And all for the want of a "+qualifier+args[0]+".")
        count+=1
    return sentence
    pass
