holes = [25, 75, 200, 50, 150]
processSize = [100, 24, 310, 50, 150]


for i in range(len(processSize)):
    alloted = 0
    
    for j in range(len(holes)):
        if(processSize[i]<= holes[j]):
            alloted = 1
            holes[j] = holes[j] - processSize[i]
            print(f"Process {i} Alloted")
            break
    
    if alloted == 0:
        print(f"Process {i} Cannot be Alloted")