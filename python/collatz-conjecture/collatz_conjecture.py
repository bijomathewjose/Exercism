def steps(number):
    
    n,count=number,0
    while n!=1:
        count+=1
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        if(n<=0):
            raise ValueError("Only positive integers are allowed")
    return count