import math
def score(x, y):
    value = math.sqrt(x**2+y**2) 
    return 10 if value<=1 else 5 if value<=5 else 1 if value<=10 else 0
#  so the x and y are the coordinates 
#  we need to find the diagonal formed by x and y 
#  since we need to check within the radius
#  so x being one side and y being other side using pythagoras theorem
#  we get the diagonal,now check if the diagonal length is as specified as radius