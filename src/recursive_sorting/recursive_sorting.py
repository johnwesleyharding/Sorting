# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    
    merged = []
    
    while len(arrA) > 0 and len(arrB) > 0:
        
        if arrA[0] > arrB[0]:
            
            merged.append(arrB.pop(0))
            
        else:
            
            merged.append(arrA.pop(0))
            
    if len(arrA) > 0:
        
        for num in arrA:
            
            merged.append(num)
        
    else:
        
        for num in arrB:
            
            merged.append(num)
        
    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    
    lng = len(arr)
    
    if lng > 1:
        
        m = lng // 2
        arrA = arr[:m]
        arrB = arr[m:]
        
        merged = merge(merge_sort(arrA), merge_sort(arrB))
    
        return merged
    
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
