def prime(number):
    prime_list=[]
    if number==0:
        raise ValueError('there is no zeroth prime')
    else:
        digit=2
        while len(prime_list)<number:
            prime_list=check_prime(digit,prime_list)
            digit+=1
    return prime_list[number-1]
    pass
def check_prime(digit,prime_list):
    if digit==2 or digit==3:
        prime_list.append(digit)
    else:
        prime=True
        for i in prime_list:
            if digit%i==0:
                prime=False
                break
        if prime:
            prime_list.append(digit)
    return prime_list