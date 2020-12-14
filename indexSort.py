# ============================================
# indexSort.
# --------------------------------------------
# Given 2 lists (arr and indices) it will order the 1st list (arr) 
# using the 2nd one (indices) as index parameters 
# indices[element in arr][order 0 for ascending or 1 to descending]
# ============================================

def indexSort(arr, indices):

    print('Original:')
    for row in arr:
        print(' '.join(map(str, row)))

    # using lambda to sort - the second sort must be inner the first one.
    arr.sort(key = lambda x:[x[r[0]] if r[1]==0 else -x[r[0]] for r in indices])


if __name__ == '__main__':

    print('>>> Starting =========  1 - indexSort ')
    print('\n')    

    # block with predefined values for test

    arr = [[3, 2, 3], [4, 2, 2], [2, 6, 2], [8, 4, 3]]
    indices = [[2, 0], [0, 1]]

    indexSort(arr, indices)

    print('Ordered:')
    for row in arr:
        print(' '.join(map(str, row)))
    
    print('\n')    
    print('>>> Finishing =========  indexSort ')
    print('\n')