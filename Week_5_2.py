def paraustu(sayi):
    coinlist = [1,5,10,25,50]
    paraus = []
    deg = 0
    for i in range(len(coinlist)):
        if(sayi == coinlist[i]):
            return sayi
        while(sayi! = 0):
            for i in range(len(coinlist)):
                if(sayi >= coinlist[i]):
                    deg = coinlist[i]
                    sayi= sayi-deg
                    paraus.append(deg)
                    return paraus
        print(paraustu(30))
        
def recMC(coinVolueList,change):
    minCoins = change
    if(change in coinVolueList):
    return 1
else:
    for i in [c for c in coinVolueList if c <= change]:
        numCoin = a+recMC(coinVolueList,change-i)
        if(numCoins<minCoin):
            minCoins = numCoins:
        return minCoins
