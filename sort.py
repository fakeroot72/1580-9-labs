def bubble(arr, cmp_less=None):
    cmp_greater = None
    if(cmp_less == None):
        cmp_greater = lambda a, b : a > b
    else:
        cmp_greater = lambda a, b : not (cmp_less(a, b) or a == b)

    n = len(arr)
    for _ in range(n):
        sorted = 0
        for i in range(n - 1):
            if(cmp_greater(arr[i], arr[i + 1])):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                sorted += 1

        if(sorted == n - 1):
            break

        sorted = 0
    return arr

def max_index(arr, l_offset, cmp_greater):
    max_val = float("-inf")
    max_i = -1
    for i in range(len(arr) - l_offset):
        if(cmp_greater(arr[i], max_val)):
            max_val = arr[i]
            max_i = i

    return [max_i, max_val]

def select(arr, cmp_less=None):
    cmp_greater = None
    if(cmp_less == None):
        cmp_greater = lambda a, b : a > b
    else:
        cmp_greater = lambda a, b : not (cmp_less(a, b) or a == b)

    n = len(arr)
    for i in range(n):
        max_i, max_val = max_index(arr, i, cmp_greater)
        if(not (max_i == n - i - 1 or max == arr[i])):
            arr[n - i - 1], arr[max_i] = max_val, arr[n - i - 1]

    return arr

def merge(arr, cmp_less=None):
    if(len(arr) == 1):
        return arr

    if(cmp_less == None):
        cmp_less = lambda a, b : a < b

    middle = len(arr) // 2
    left_arr = merge(arr[:middle])
    right_arr = merge(arr[middle:])

    lindex = 0
    rindex = 0
    while(lindex < len(left_arr) and rindex < len(right_arr)):
        if(cmp_less(left_arr[lindex], right_arr[rindex])):
            arr[lindex + rindex] = left_arr[lindex]
            lindex += 1
        else:
            arr[lindex + rindex] = right_arr[rindex]
            rindex += 1

    arr[lindex + rindex + 1:] = left_arr[lindex:] + right_arr[rindex:]
    return arr
