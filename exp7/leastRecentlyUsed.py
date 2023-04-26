# referenceStr = [1, 3, 0, 3, 5, 6, 3]
referenceStr = [1, 2, 1, 0, 3, 0, 4, 2, 4]
allPrSet = set(referenceStr)
apd = {i:1000 for i in allPrSet}

m = 3
n = len(referenceStr)
slots = []

totalHit = 0
totalMiss = 0

for i in range(n):
    a = referenceStr[i]
    
    if a not in slots:
        if len(slots) != m:
            slots.append(a)
            print("Page Miss")
            apd[a] = i
            totalMiss += 1
        else:
            minKey = min(apd, key=lambda k: apd[k])
            slots.remove(minKey)
            apd[minKey] = 1000
            slots.append(a)
            print("Page Miss")
            totalMiss += 1
            
            
    else:
        print("Page Hit")
        totalHit += 1
            
print(f"Miss Ratio: {totalMiss/n}")
print(f"Hit Ratio: {totalHit/n}")

