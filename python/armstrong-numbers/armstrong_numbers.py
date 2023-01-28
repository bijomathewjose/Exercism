def is_armstrong_number(number):
    string=str(number)
    sumed=sum( int(i)**len(string) for i in string )
    return sumed==number