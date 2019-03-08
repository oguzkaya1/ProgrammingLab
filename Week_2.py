
def my_search_selection(my_array):
    swap_count=0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(i,i+1):
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_count=swap_count+1
    print("number of exchange :",swap_count)
    return
------------------------------------------------------------------
def my_binary_search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        #print("first - last",first,last)
        s=s+1
        if(my_sorted_array[midpoint]==item):
            found=True
        else:
            if(item<my_sorted_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
    return found,midpoint,s
------------------------------------------------------------------
def fibo_loop(n):
    a,b=0,1
    if(n==0):
        return 0
    for i in range(n-1):
        a,b=b,a+b
    return b
------------------------------------------------------------------
def fibo_recursive(n):
    if(n<2):
        return n
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
------------------------------------------------------------------    
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
------------------------------------------------------------------
def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)
------------------------------------------------------------------
def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)
------------------------------------------------------------------
def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)
    
