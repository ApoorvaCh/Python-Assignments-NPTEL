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
        pos = i
        while pos > 0 and arr[pos] < arr[pos-1]:
            (arr[pos], arr[pos-1]) = (arr[pos-1], arr[pos])
            pos = pos-1
    return arr


if __name__ == "__main__":
    ele_list = list(map(int, input("Enter the list of elements to be sorted: ").split(' ')))
    sorted_list = insertion_sort(ele_list)
    for i in sorted_list:
        print(i, end=' ')
    print()