# Straight Merging Sort Implementation in Python

def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays of arr.
    First subarray is arr[left:mid+1]
    Second subarray is arr[mid+1:right+1]
    """
    # Create temporary arrays
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def straight_merging_sort(arr):
    """
    Perform Straight Merging Sort on arr.
    """
    n = len(arr)
    size = 1  # Initial size of subarrays to merge

    # Merge subarrays in bottom up manner
    while size < n:
        left = 0
        while left < n-1:
            mid = min(left + size - 1, n-1)
            right = min(left + 2*size - 1, n-1)
            if mid < right:
                merge(arr, left, mid, right)
            left += 2*size
        size *= 2

# Example usage
if __name__ == "__main__":
    # Example array to sort
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    straight_merging_sort(arr)
    print("Sorted array:", arr)
