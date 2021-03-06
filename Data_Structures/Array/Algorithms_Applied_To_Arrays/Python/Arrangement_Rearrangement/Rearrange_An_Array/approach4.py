"""
    Problem Explonation:
    -------------------
        Given an array of elements of length N, ranging from 0 to N – 1.
        All elements may not be present in the array.
        If the element is not present then there will be -1 present in the array.
        Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

        Examples:
        --------

            Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
            Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

            Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
                        11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
            Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19]

================================================================================

    Approach Explonation (Swap elements in Array):
    ---------------------------------------------
        1) Iterate through elements in an array 
        2) If arr[i] >= 0 && arr[i] != i, put arr[i] at i ( swap arr[i] with arr[arr[i]])

    Time Complexity:
    ---------------
        O(n)

"""


def fixArray(arr):
    i = 0
    while i < len(arr):
        if arr[i] >= 0 and arr[i] != i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1


arr1 = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(f"Original array: {arr1}")
fixArray(arr1)
print(f"Array after calling function: {arr1}")
print("=====================")


arr2 = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
print(f"Original array: {arr2}")
fixArray(arr2)
print(f"Array after calling function: {arr2}")
