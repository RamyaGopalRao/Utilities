arr=[3, 1, 4, 6, 5]
import math
def checkpyth(a,b,c):
    prd=math.pow(a,2)+math.pow(b,2)
    return math.pow(c,2)==prd

def findpythagorean(arr):
    pythagoreanarra=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if checkpyth(arr[i],arr[j],arr[k]):
                    pythagoreanarra.append((arr[i],arr[j],arr[k]))
    return pythagoreanarra

print(findpythagorean(arr))
