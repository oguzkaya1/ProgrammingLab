def my_vector_scalar_product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]
    return my_result
#-------------------------------------------
def my_vector_substraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]-w[i]
    return my_result
#-------------------------------------------
def my_vector_addition(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]+w[i]
    return my_result
#-------------------------------------------
def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t
#-------------------------------------------
def frequency_table(list1):
    freq={}
    for i in list1:
        if(i in freq):
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    return freq
#-------------------------------------------
def frequency_table_2(list2):
    frequency_list=[]
    for i in range(len(list2)):
        s=False
        for j in range(len(frequency_list)):
            if(list2[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
                frequency_list.append([list2[i],1])
    return frequency_list

