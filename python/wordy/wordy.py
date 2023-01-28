def answer(question):
    question=question.replace("What is ","").replace("?","").replace("plus","+").replace("minus","-").replace('multiplied by',"*").replace("divided by","/").split(" ");
    question.insert(0,"(")
    question.insert(4,")")
    print(("").join(question))
    q=[i.isalpha() for i in question if i not in ("What", "is")]
    if any(q):
        raise ValueError("unknown operation")
    try:
        return eval((" ").join(question))
    except:
        raise ValueError("syntax error")
    pass
#copied from daros21's