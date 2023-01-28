RES={'black': '0','brown': '1','red': '2','orange': '3','yellow': '4','green': '5','blue': '6','violet': '7','grey': '8','white': '9'}
WGT={0:' ',1:'0 ',2:'00 ',3:' kilo',4:'0 kilo',5:'00 kilo',6:' mega',7:'0 mega',8:'00 mega',9:' giga'}
def label(colors):
    val=""
    count=int(RES[colors[2]])
    for i in range(2):
        if colors[i]=='black':   
            count+=1
        else:
            val+=RES[colors[i]]
    return val+WGT[count]+"ohms"
    pass