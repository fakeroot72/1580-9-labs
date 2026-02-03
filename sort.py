#!/usr/bin/python

############################################################################
# ЭТОТ КОД НАПИСАН МНОЮ, ГРИГОРЬЕВОМ ЕВГЕНИЕМ ОЛЕГОВИЧЕМ, А НЕ НЕЙРОСЕТЬЮ. #
############################################################################

from random import random, randint

def clone(arr):
    arr2 = []
    for i in arr:
        arr2.append(i)
    return arr2

def bubble(arr):
    n = len(arr)
    comps = 0
    permuts = 0
    for _ in range(n):
        sorted = 0
        for i in range(n - 1):
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                permuts += 1
            else:
                sorted += 1
            comps += 1

        if(sorted == n - 1):
            break
        sorted = 0
    return [arr, comps, permuts]

def max_index(arr, l_offset):
    max_val = float("-inf")
    max_i = -1
    for i in range(len(arr) - l_offset):
        if(arr[i] > max_val):
            max_val = arr[i]
            max_i = i
    return [max_i, max_val]

def select(arr):
    n = len(arr)
    comps = 0
    permuts = 0
    for i in range(n):
        max_i, max_val = max_index(arr, i)
        if(not (max_i == n - i - 1 or max == arr[i])):
            arr[n - i - 1], arr[max_i] = max_val, arr[n - i - 1]
        permuts += 1
        comps += n - i
    return [arr, comps, permuts]

def merge(arr):
    if(len(arr) == 1):
        return [arr, 1, 0]

    middle = len(arr) // 2
    left_arr, lcomps, lpermuts = merge(arr[:middle])
    right_arr, rcomps, rpermuts = merge(arr[middle:])
    comps = lcomps + rcomps
    permuts = lpermuts + rpermuts

    merged = []
    while(len(left_arr) > 0 and len(right_arr) > 0):
        if(left_arr[0] < right_arr[0]):
            merged.append(left_arr.pop(0))
        else:
            merged.append(right_arr.pop(0))
        comps += 3
        permuts += 1

    merged += left_arr + right_arr
    permuts += 1
    arr = merged
    return [arr, comps, permuts]

def random_number(min_num, max_num):
    return round(min_num + (max_num - min_num) * random(), 5)

def check_int(num, name):
    if(not (num.replace('-', '').isnumeric() and num.count('-') <= 1)):
        print("\x1b[31mERROR: \x1b[0m " + name + " is not a whole number")
        return 2
    return 0

def check_float(num, name):
    if(not (((num[0] == "-" and num.count("-") == 1) or num.count('-') == 0) and num.count(".") <= 1 and num.replace('-', '').replace('.', '').isnumeric())):
        print("\x1b[31mERROR: \x1b[0m " + name + " is not a number")
        return 2
    return 0

def main():
    mode = input("mode: ")
    if(mode == "interactive"):
        rand_range = [0, 0]
        asked_rand = 0;
        arr = input("array of numbers(r for random): ").split()
        for i in range(len(arr)):
            if(arr[i] == "r"):
                if(not asked_rand):
                    rand_range = input("random range from to: ").split()
                    if(len(rand_range) != 2):
                        print("\x1b[31mERROR: \x1b[0mrange is exactly 2 numbers")
                        return 2

                    asked_rand = 1
                    if(check_float(rand_range[0], "\"" + rand_range[0] + "\"") != 2 and check_float(rand_range[1], "\"" + rand_range[1] + "\"") != 2):
                        rand_range = sorted(list(map(float, rand_range)))

                    else:
                        return 2

                arr[i] = random_number(rand_range[0], rand_range[1])

            elif(check_float(arr[i], "\"" + arr[i] + "\"") != 2):
                arr[i] = float(arr[i])
            else:
                return 2

        sort = input("sorting method: ")
        if(sort != "bubble" and sort != "select" and sort != "merge"):
            print("\x1b[31mERROR: \x1b[0munknown sorting method: " + sort)
            print("available modes: bubble, select, merge")
            return 2

        comps = 0
        permuts = 0
        if(sort == "bubble"):
            arr, comps, permuts = bubble(arr)

        if(sort == "select"):
            arr, comps, permuts = select(arr)

        if(sort == "merge"):
            arr, comps, permuts = merge(arr)

        print("comparisons: " + str(comps))
        print("permutations: " + str(permuts))
        print("sorted: " + str(arr))
        return 0

    elif(mode == "demo"):
        arr = [randint(0, 99) for _ in range(15)]

        sort = input("sorting method: ")
        if(sort != "bubble" and sort != "select" and sort != "merge"):
            print("\x1b[31mERROR: \x1b[0munknown sorting method: " + sort)
            print("available modes: bubble, select, merge")
            return 2

        print("unsorted: " + str(arr))
        comps = 0
        permuts = 0
        if(sort == "bubble"):
            arr, comps, permuts = bubble(arr)

        if(sort == "select"):
            arr, comps, permuts = select(arr)

        if(sort == "merge"):
            arr, comps, permuts = merge(arr)

        print("comparisons: " + str(comps))
        print("permutations: " + str(permuts))
        print("sorted: " + str(arr))
        return 0

    elif(mode == "test"):
        tests = input("how many tests: ")
        if(check_int(tests, "tests") == 2):
            return 2

        tests = int(tests)
        if(tests < 0):
            print("\x1b[31mERROR: \x1b[0mtests cannot be less than 0")
            return 2

        if(tests == 0):
            print("\x1b[33mWARN: \x1b[0mno tests executed")

        min_len = input("minimum lenght: ")
        if(check_float(min_len, "lenght") == 2):
            return 2

        min_len = int(min_len)
        if(min_len < 0):
            print("\x1b[31mERROR: \x1b[0mlenght cannot be less than 0")
            return 2

        max_len = input("maximum lenght: ")
        if(check_float(max_len, "lenght") == 2):
            return 2

        max_len = int(max_len)
        if(max_len < 0):
            print("\x1b[31mERROR: \x1b[0mlenght cannot be less than 0")
            return 2

        if(min_len > max_len):
            print("\x1b[31mERROR: \x1b[0mminimum lenght should be less or equal than maximum")
            return 2

        min_val = input("minimum value: ")
        if(check_float(min_val, "value") == 2):
            return 2

        min_val = float(min_val)
        max_val = input("maximum value: ")
        if(check_float(max_val, "value") == 2):
            return 2

        max_val = float(max_val)
        if(min_val > max_val):
            print("\x1b[31mERROR: \x1b[0mminimum value should be less or equal than maximum")
            return 2

        for _ in range(tests):
           arr_bubble = [random_number(min_val, max_val) for _ in range(round(random_number(min_len, max_len)))]
           arr_select = clone(arr_bubble)
           arr_merge = clone(arr_bubble)
           arr_sort = clone(arr_bubble)
           arr_sort.sort()
           bubble(arr_bubble)
           select(arr_select)
           arr_merge = merge(arr_merge)[0]
           if(arr_bubble != arr_sort or arr_select != arr_sort or arr_merge != arr_sort):
               print("\x1b[31mFAIL!\x1b[0m")
               print("expected: " + str(arr_sort))
               if(arr_bubble != arr_sort):
                   print("got from bubble: " + str(arr_bubble))

               if(arr_select != arr_sort):
                   print("got from select: " + str(arr_select))

               if(arr_merge != arr_sort):
                   print("got from merge: " + str(arr_merge))

               return 1

        print("\x1b[32mAll tests passed\x1b[0m")
        return 0

    else:
        print("\x1b[31mERROR: \x1b[0munknown mode")
        print("list of modes: interactive, demo, test")
        return 2

def main_wrapper():
    while(True):
        exit = main()
        i = 0
        while(True):
            again = input("sort again or exit? (y/n): ")
            if(again == "n"):
                return exit
            elif(again == "y"):
                break
            else:
                if(i >= 10):
                    print("press y and then press enter to use the program again")
                    print("press n and then press enter to exit the program")
                print("y - sort again, n - exit")
                i += 1

if(__name__ == "__main__"):
    import sys
    sys.exit(main_wrapper())

