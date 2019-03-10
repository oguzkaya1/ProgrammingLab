def selection_sort(my_array):
  swap_count=0                         
  for i in range(len(my_array)-1,0,-1):
    positionOfMax=0
    for location in range(0,i+1,1):
      if(my_array[location]>my_array[positionOfMax]):
        positionOfMax=location
    temp=my_array[location]
    my_array[location]=my_array[positionOfMax]
    my_array[positionOfMax]=temp
    swap_count=swap_count+1
  print("number of exchange :",swap_count)

my_array=[9,8,7,6,5,4,3,2,1]

selection_sort(my_array)
print(my_array)
print("\n")


def binary_search(my_array,item):
  bulundu="Sayi Mevcut"
  bulunmadi="Sayi Mevcut Degil"
  first=0                              
  last=len(my_array)-1                  
  found=False
  step=0                               
  while first<=last and not found:
    midpoint=(first+last)//2
    step=step+1
    if(my_array[midpoint]==item):
      found=True
    else:
      if(item<my_array[midpoint]):
        last=midpoint-1
      else:
        first=midpoint+1
    if(found==True):
        return bulundu,midpoint,step
    else:
        return bulunmadi,midpoint,step
  
