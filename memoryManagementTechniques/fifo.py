# m = int(input("Enter the number of memory slots: "))
m =3
referenceStr = [1, 3, 0, 3, 5, 6, 3]
n=len(referenceStr)

slots = []

totalMiss = 0
totalHit = 0

for i in range(len(referenceStr)):
    a = referenceStr[i]
    
    
    if a not in slots:
        if(len(slots) != m):
            slots.append(a)
            print("Page Miss")
            totalMiss = totalMiss +1
        else:    
            print("Page Miss")
            slots.remove(slots[0])
            slots.append(a)
            totalMiss = totalMiss + 1
            
    else:
        print("Page hit")
        totalHit = totalHit + 1
        
print(f"Hit Ratio: {totalHit/n}")
print(f"Miss Ratio: {totalMiss/n}")
