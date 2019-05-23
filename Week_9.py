def recMC(coinValueList,change,knownResults):
    minCoins = change
    
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else :
        for i in [c for c in coinValueList if c<= change]:#bozuk para listesi olustur
            numCoins = 1 + recMC(coinValueList, change-i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins
    
recMC(bozukluklar, 40,[0]*41)
