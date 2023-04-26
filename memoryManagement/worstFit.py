holes = [25, 75, 200, 50, 150]
processSize = [100, 24, 10, 50, 150]


print(f"Holes before: {holes}")
for i in range(len(processSize)):
    maxIndex = holes.index(max(holes))
    
    if ( processSize[i]<= holes[maxIndex]):
        print(f"Process {i} Alloted")
        holes[maxIndex] = holes[maxIndex]-processSize[i]
        
    else:
        print(f"Process {i} Cannot be Alloted")

print(f"Holes Now: {holes}")