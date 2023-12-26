""" Insertion Sort."""


def insertion_sort(arr: list) -> list:
    """
    sort the elements in ascending order using insertion sort technique.

    Args:
        arr: A list of elements to be stored.

    Returns:
        Sorted array.
    """

    for i in range(len(arr)):
        for j in range(i):
            if(arr[j] >= arr[i]):
                ele = arr[i]
                arr.remove(ele)
                arr.insert(j, ele)
                break
    return arr


if __name__ == "__main__":
    ele_list = list(map(int, input("Enter the list of elements to be sorted: ").split(' ')))
    sorted_list = insertion_sort(ele_list)
    for i in sorted_list:
        print(i, end=' ')
    print()