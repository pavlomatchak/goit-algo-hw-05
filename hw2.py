def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    loops = 0

    if upper_bound < x:
        return -1

    while low <= high:
        loops += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        else:
            return (loops, arr[mid])

    return (loops, upper_bound)


if __name__ == '__main__':
    arr = [3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 23

    result = binary_search(arr, x)

    if result != -1:
        print(result)
    else:
        print("Number is out of range")
