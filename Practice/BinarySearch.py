def binarySearch(arr, s, low, high):
    mid = (low + high)//2
    if (low <= high):
        if (s == arr[mid]):
            return True
        elif (s < arr[mid]):
            return binarySearch(arr, s, low, mid)
        else:
            return binarySearch(arr, s, mid+1, high)
    else:
        return False


def search(arr, s):
    low = 0
    high = len(arr) - 1
    return binarySearch(arr, s, low, high)


if __name__ == '__main__':
    arr = list(map(int, input('Enter the list of elements: ').split(' ')))
    s = int(input('Enter the element you want to search: '))
    print(search(arr, s))

# Time Complexity = O(logn).
