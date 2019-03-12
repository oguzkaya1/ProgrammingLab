def carpanulma(sayi):
  liste=[]
  i=2
  while(sayi!=1):
    if(sayi%i==0):
      sayi=sayi/i
      liste.append(i)
    else:
    i=i+1
  return liste
  
