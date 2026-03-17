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
        comps += n - 1
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
    lindex = 0
    rindex = 0
    while(lindex < len(left_arr) and rindex < len(right_arr)):
        if(left_arr[lindex] < right_arr[rindex]):
            merged.append(left_arr[lindex])
            lindex += 1
        else:
            merged.append(right_arr[rindex])
            rindex += 1
        comps += 1
        permuts += 1

    merged += left_arr[lindex:] + right_arr[rindex:]
    permuts += 1
    arr = merged
    return [arr, comps, permuts]

def random_number(min_num, max_num):
    return round(min_num + (max_num - min_num) * random(), 5)

def check_int(num):
    if(not (num.replace('-', '').isnumeric() and num.count('-') <= 1)):
        print(f"\x1b[31mERROR: \x1b[0m \"{num}\"  is not a whole number")
        return 2
    return 0

def check_float(num):
    if(not (((num[0] == "-" and num.count("-") == 1) or num.count('-') == 0) and num.count(".") <= 1 and num.replace('-', '').replace('.', '').isnumeric())):
        print(f"\x1b[31mERROR: \x1b[0m \"{num}\" is not a number")
        return 2
    return 0

def check_number_array(arr):
    err = 0
    for i in arr.split():
        if(i != 'r'):
            err |= check_float(i)
    return err

def check_range(rng):
    rng = rng.split()
    if(len(rng) != 2):
        print("\x1b[31mERROR: \x1b[0mrange is exactly 2 numbers")
        return 2

    return check_float(rng[0]) | check_float(rng[1])

def check_sort(sort):
    if(sort != "bubble" and sort != "select" and sort != "merge"):
        print("\x1b[31mERROR: \x1b[0munknown sorting method: " + sort)
        print("available modes: bubble, select, merge")
        return 2

    return 0

def check_tests(tests):
    if(check_int(tests) == 2):
        return 2

    tests = int(tests)
    if(tests < 0):
        print("\x1b[31mERROR: \x1b[0mtests cannot be less than 0")
        return 2

    return 0


def check_length(ln):
    if(check_int(ln) == 2):
        return 2

    ln = int(ln)
    if(ln < 0):
        print("\x1b[31mERROR: \x1b[0mlength cannot be less than 0")
        return 2

    return 0

def check_input(request, checkers):
    value = ""
    incorrect = 1
    while(incorrect):
        incorrect = 0
        value = input(request)
        for check in checkers:
            incorrect |= check(value)

    return value



def main():
    while(True):
        mode = input("mode: ")
        if(mode == "interactive"):
            rand_range = (0, 0)
            asked_rand = False;
            arr = check_input("array of numbers(r for random): ", (check_number_array,)).split()
            for i in range(len(arr)):
                if(arr[i] == "r"):
                    if(not asked_rand):
                        rand_range = tuple(map(int, check_input("random range from to: ", (check_range,)).split()))
                        asked_rand = True

                    arr[i] = random_number(rand_range[0], rand_range[1])

                else:
                    arr[i] = float(arr[i])

            sort = check_input("sorting method: ", (check_sort,))

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
            arr_bubble = [randint(0, 99) for _ in range(15)]
            arr_select = clone(arr_bubble)
            arr_merge = clone(arr_bubble)

            print("unsorted: " + str(arr_bubble))
            comps_bubble = 0
            permuts_bubble = 0
            comps_select = 0
            permuts_select = 0
            comps_merge = 0
            permuts_merge = 0
            arr_bubble, comps_bubble, permuts_bubble = bubble(arr_bubble)
            arr_select, comps_select, permuts_select = select(arr_select)
            arr_merge, comps_merge, permuts_merge = merge(arr_merge)
            print("sorted bubble: " + str(arr_bubble))
            print("sorted select: " + str(arr_select))
            print("sorted merge:  " + str(arr_merge))
            print("comparisons bubble: " + str(comps_bubble))
            print("permutations bubble: " + str(permuts_bubble))
            print("comparisons select: " + str(comps_select))
            print("permutations select: " + str(permuts_select))
            print("comparisons merge: " + str(comps_merge))
            print("permutations merge: " + str(permuts_merge))
            return 0

        elif(mode == "test"):
            tests = int(check_input("how many tests: ", (check_tests,)))

            if(tests == 0):
                print("\x1b[33mWARNING: \x1b[0mno tests executed")

            min_len = 0
            max_len = 0
            # can't get rid of this while
            while(True):
                min_len = int(check_input("minimum length: ", (check_length,)))
                max_len = int(check_input("maximum length: ", (check_length,)))
                if(min_len > max_len):
                    print("\x1b[31mERROR: \x1b[0mminimum length should be less or equal than maximum")
                    continue
                break

            min_val = 0
            max_val = 0
            while(True):
                min_val = float(check_input("minimum value: ", (check_float,)))
                max_val = float(check_input("maximum value: ", (check_float,)))
                if(min_val > max_val):
                    print("\x1b[31mERROR: \x1b[0mminimum value should be less or equal than maximum")
                    continue
                break

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
            continue

        return 0

def main_wrapper():
    try:
        while(True):
            exit = 0
            try:
                exit = main()
            except EOFError:
                return 0

            i = 0
            while(True):
                try:
                    again = input("sort again or exit? (y/n): ")
                except EOFError:
                    return 0
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
    except KeyboardInterrupt:
        return 0

if(__name__ == "__main__"):
    import sys
    sys.exit(main_wrapper())
