# Considering The List/ Array is Sorted

def binary_search(list, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(list) - 1
    if high < low:      #to avoid RecursionError
        return -1;

    mid_point = (low + high) // 2  # floor division

    if list[mid_point] == target:
        return mid_point
    elif target < list[mid_point]:
        return binary_search(list, target, low, mid_point - 1)
    else:
        # i.e. target > list[mid_point]
        return binary_search(list, target, mid_point + 1, high)



if __name__ == '__main__':
    list = list()
    n = int(input("Enter How many numbers are there in the list:\n"))
    print("Enter the elements of the list: \n")
    for i in range(0, n):
        a = int(input("<"))
        list.append(a)
    list.sort()
    target = int(input("Enter the Value to be searched: "))
    print("{} found at {} index".format(target, binary_search(list, target)))
