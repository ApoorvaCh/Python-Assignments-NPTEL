'''
1. first we need to find the minimum from the list
2. swap the min with 1st element
3. next find 2nd min and swap it with second element and so on..
'''


def getMinIndex(arr):
    min_index = 0
    for i in range(len(arr)):
        if (arr[min_index] > arr[i]):
            min_index = i
    return min_index


def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_ele_ind = i + getMinIndex(arr[i:n])
        arr[i], arr[min_ele_ind] = arr[min_ele_ind], arr[i]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input('Enter the elements to sort: ').split(' ')))
    arr = SelectionSort(arr)
    print("After sorting: ", end=" ")
    for i in arr:
        print(i, end=' ')
    print()

# Time Complexity = O(n^2)
