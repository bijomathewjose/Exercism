RNA={'AUG':'Methionine','UUU':'Phenylalanine','UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','UCU':'Serine','UCC':'Serine','UCA':'Serine','UCG':'Serine','UAU':'Tyrosine','UAC':'Tyrosine','UGU':'Cysteine', 'UGC':'Cysteine','UGG':'Tryptophan','UAA':'STOP', 'UAG':'STOP','UGA':'STOP'}
def proteins(strand):
    n=len(strand)//3
    pieces=[RNA[strand[i*3-3:i*3]] for i in range(1,n+1)]
    ret=[]
    for i in pieces:
        if i=='STOP':
            break
        ret.append(i)
    return ret
    pass
