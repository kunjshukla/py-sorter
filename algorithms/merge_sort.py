def merge_sort(unsortedList):
    if len(unsortedList) > 1:
        mid = len(unsortedList) // 2
        leftList = unsortedList[:mid]
        rightList = unsortedList[mid:]
       
    
        merge_sort(leftList)
        merge_sort(rightList)

         
        m = 0
        n = 0
        
        z = 0

        while m < len(leftList) and n < len(rightList):
            if leftList[m] <= rightList[n]:
        
              unsortedList[z] = leftList[m]
        
              m += 1
            else:
                unsortedList[z] = rightList[n]
                n += 1
            z += 1

        
        while m < len(leftList):
            unsortedList[z] = leftList[m]
            m += 1
            z += 1

        while n < len(rightList):
            unsortedList[z]=rightList[n]
            n += 1
            z += 1
    return unsortedList