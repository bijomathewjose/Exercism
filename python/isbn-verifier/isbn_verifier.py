def is_valid(isbn):
    if len(isbn)<10 or len(isbn.replace('-',''))>10:
        return False
    index=10
    sum=0
    for number in isbn:
        if number in ['0','1','2','3','4','5','6','7','8','9']:
            sum+=int(number)*index
            index-=1
        elif number == 'X':
            sum+=10
        elif number =='-':
            continue
        else:
            return False
    return sum%11==0
    pass
