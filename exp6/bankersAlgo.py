# n = int(input("No of processes: "))
# m = int(input("No of Types of resources: "))

n = 5
m = 4


processes=[i for i in range(n)]
allocated = [[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
maxreq = [[0, 0, 1, 2], [1, 7, 5, 0], [4, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]]
available = [[1, 5, 2, 0]]
safeSeq = []

need = [[(maxreq[i][j]-allocated[i][j]) for j in range(m)]for i in range(n)]
totalResources = [[0, 0, 0, 0]] #[A, B, C, D]
a = available[0][0]
b = available[0][1]
c = available[0][2]
d = available[0][3]

for i in range(n):
    a = a + allocated[i][0]
    b = b + allocated[i][1]
    c = c + allocated[i][2]
    d = d + allocated[i][3]
    
totalResources = [[a, b, c, d]]
    


while True:
    
    if(available == totalResources):
        if(len(safeSeq) == n):
            print(f"Safe Sequence: {safeSeq}")
            break
        else:
            print('Safe Sequence is not possible with these processes')
    
    
    satifaction = [0 for i in range(n)]
    
    for j in range(n):
        f=0
        for k in range(m):
            if need[j][k] <= available[0][k]:
                f = 1
            else:
                f = 0
                break
        
        if (f == 1 and j not in safeSeq):
            satifaction[j] = 1
        
    #When asked for more than total resources    
    if(1 not in satifaction):
        print("Safe Sequence not possible.")
        break
        
    ind = satifaction.index(1)
    safeSeq.append(ind)
    available = [[available[0][j]+allocated[ind][j] for j in range(m)]]        
    
print(totalResources)
