def square_of_sum(number):
    x=(number/2)*(number+1)
    return x**2
    pass
    
def sum_of_squares(number):
    sum=0
    for i in range(number):
        sum+=(i+1)**2
    return sum
    pass

def difference_of_squares(number):
    return abs(sum_of_squares(number)-square_of_sum(number))
    pass
