def square_root(number):
    if number==1:
        return 1
    n=number//2
    while n*n>number:
        n=n//2
    while n<number:
        if n*n==number:
            return n
        n+=1
    pass