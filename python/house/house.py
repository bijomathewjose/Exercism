def recite(start_verse, end_verse):
    verse={1:("","house that Jack built."),2:("ate","malt"),3:("killed","rat"),4:("worried","cat"),5:("tossed","dog"),6:("milked","cow with the crumpled horn"),7:("kissed","maiden all forlorn"),8:("married","man all tattered and torn"),9:("woke","priest all shaven and shorn"),10:("kept","rooster that crowed in the morn"),11:("belonged to","farmer sowing his corn"),12:("","horse and the hound and the horn")}
    para=[]
    sentence=""
    for i in range(start_verse,end_verse+1):
        sentence="This is the "+verse[i][1]+(" " if i!=1 else "")
        if i>2:
            for j in range(i-1,1,-1):
                sen="that "+verse[j][0]+" the "+verse[j][1]+" "
                sentence+=sen
        sentence+="that lay in the house that Jack built." if i!=1 else ""
        para.append(sentence)
        sentence=""
    print(para)
    return para
    pass
