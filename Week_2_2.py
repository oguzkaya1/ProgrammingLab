def fib_loop(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a
    

def fib_recursive(n):
    if(n<2):
        return n
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)

       

def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s


def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)
   

def power_loop(m,n):#m^n
    s=m
    for i in range(1,n):
        s=s*m
    return s
     

def power_recursive(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return power_recursive(m*m,int(n/2))
    elif(n%2!=0):
        return power_recursive((m*m),int(n/2))*m
