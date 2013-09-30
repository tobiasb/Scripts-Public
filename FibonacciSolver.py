import time

def FibRec(index):
    if index == 0: return 0
    if index == 1: return 1
    return FibRec(index-1)+FibRec(index-2)

fibs = [0,1]
def FibIter(index):
    for x in range(len(fibs),index+1):
        fibs.append(fibs[x-1]+fibs[x-2])
    return fibs[index]

for x in range(0,100000000):
    start = time.clock()
    print(str(x) + "\t" + str(FibRec(x)) + "\t" + str(time.clock() - start))
    #print(str(x) + "\t" + str(FibIter(x)))
    
#42