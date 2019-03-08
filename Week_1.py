
import random
def generate_an_array(n):
    my_array=[]
    for i in range(n):
        s=random.randint(0,100)
        my_array.append(s)
    return my_array
#-----------------------------------------------
for i in range(len(my_arr_1)):
    print(i,":",my_arr_1[i])
print("\n")
#-----------------------------------------------
def print_an_array(my_arr_1):
    for item in my_arr_1:
        print(item, end=" ")  
#-----------------------------------------------
def my_bubble_sort(my_array):
    for i in range(len(my_arr_1)-1,0,-1):
        for j in range(i):
            if(my_arr_1[j]>my_arr_1[j+1]):
                t=my_arr_1[j]
                my_arr_1[j]=my_arr_1[j+1]
                my_arr_1[j+1]=t
#-----------------------------------------------
def search_an_array(my_array,n):
    found=False
    step=0
    for i in range(len(my_array)):
        if(my_array[i]==n):
            found=True
            step=i
    if(found==False):
        print("\nnot found")
    else:
        print("\n","found:",found,"step:",step)



