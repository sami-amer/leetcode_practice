def mergeArray(arr1,arr2): # *NOTE: G4G Solution for merging two sorted arrays, which is just the merge portion of a merge-sort
    n1 = len(arr1)
    n2 = len(arr2)

    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
 
    # Traverse both array
    while i < n1 and j < n2:
     
        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
     
 
    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1
 
    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    
    return arr3

def findMedianSortedArrays(nums1, nums2): # *NOTE: the median is slighlty different if the list is even or odd length
    arr = mergeArray(nums1, nums2)
    if len(arr)%2 == 0:
        return (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1]) /2
    else:
        return (arr[int(len(arr)/2)])

if __name__ == '__main__':
    n1 = [1,3]
    n2= [2]
    print(findMedianSortedArrays(n1,n2))