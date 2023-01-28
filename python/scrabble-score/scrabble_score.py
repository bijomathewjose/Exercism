def score(word):
    word_list=[('AEIOULNRST',1),('DG',2),('BCMP',3),('FHVWY',4),('K',5),('JX',8),('QZ',10)]
    val=0
    for i in word:
        for j in word_list:
            print(j[0])
            if i.upper() in j[0]:
                print(j)
                val+=j[1]
    return val
    pass
