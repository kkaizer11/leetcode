#Given an array of integers arr, return true if the number of 
#occurrences of each value in the array is unique or false otherwise.

# Input: arr = [1,2,2,1,1,3]
# Output: true

# Input: arr = [1,2]
# Output: false

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

def uniqueOccurrences(arr:list[int])->bool::
    dicio = {}
    for i in arr:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    if len(dicio.values()) == len(set(dicio.values())):
        return True
    return False
