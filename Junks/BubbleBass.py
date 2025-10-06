array = [5,3,1,2,4]
def bubbleSort(array):
    made_a_swap = True 
    n = len(array)
    
    while made_a_swap:
        made_a_swap = False 
        
        for i in range(n-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp 
                made_a_swap = True 
                
            return array