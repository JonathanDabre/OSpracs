holes = [25, 75, 200, 50, 150]
processSize = [100, 24, 10, 50, 250]    
    
for i in range(len(processSize)):
    a= processSize[i]
    diff = [holes[i]-a for i in range(len(holes))]
    positiveDiff = [x for x in diff if x>=0]
    
    if(len(positiveDiff) ==0):
        print(f"Process {i} Cannot be alloted")
    else:
        bestFitIndex = diff.index(min(positiveDiff))
        holes[bestFitIndex] = holes[bestFitIndex]-processSize[i]
        print(f"Process {i} Alloted")
    
    