# TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):
    
    for i in range(len(arr) - 1):
        
        s = i
        
        for j in range(i + 1, len(arr)):
            
            if arr[j] < arr[s]:
                
                s = j
                
        if s != i:
            
            hold = arr[i]
            arr[i] = arr[s]
            arr[s] = hold
    
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    
    while True:
        
        flag = 0
        
        for i in range(len(arr) - 1):
            
            if arr[i] > arr[i + 1]:
                
                hold = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = hold
                flag = 1
                
        if flag == 0:
            
            return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
    
    minv = arr[0]
    minc = 0
    maxv = arr[0]
    maxc = 0
    
    for i in range(len(arr)):
        
        if arr[i] < minv:
            
            minv, minc = arr[i], 1
            
        elif arr[i] > maxv:
            
            maxv, maxc = arr[i], 1
            
        elif arr[i] == minv:
            
            minc += 1
            
        elif arr[i] == maxv:
            
            maxc += 1
            
    if maxv != minv:
        
        if minc + maxc < len(arr):
            
            other = []
            
            for val in arr:
                
                if val != minv and val != maxv:
                    
                    other.append(val)
                
            return [minv] * minc + count_sort(other) + [maxv] * maxc
        
        return [minv] * minc + [maxv] * maxc

    return arr