# STRETCH: implement Linear Search				
def linear_search(target, search_set):
    
    for i in range(len(search_set)):
        
        if target == search_set[i]:
            
            return i
    
    return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(target, search_set):
    
    lng = len(search_set)
    mid = lng // 2
    below = search_set[:mid]
    val = search_set[mid]
    above = search_set[mid + 1:]
    
    if lng < 2 and target != val:
        
        return -1
    
    if target < val:
        
        ind = binary_search(target, below)
                
    elif target > val:

        ind = binary_search(target, above)
        
    elif target == val:
        
        return mid
    
    return ind


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

