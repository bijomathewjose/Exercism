def convert(number):
    string='Pling' if number%3==0 else ""
    string+='Plang' if number%5==0 else ""
    string+='Plong' if number%7==0 else ""
    return string if string!="" else str(number)
