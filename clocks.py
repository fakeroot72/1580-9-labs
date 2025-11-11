#!/usr/bin/python
import sys

def ending(n, type):
    if(type != "m" and type != "f"):
        return "err"

    n = abs(n)
    if(n % 10 > 4 or n % 10 == 0 or 10 < n % 100 < 20):
        return "ов" if type == 'm' else ""
    elif(n % 10 == 1):
        return "" if type == 'm' else "а"
    else:
        return "а" if type == 'm' else "ы"

def mins_to_str(hr, min, total_mins):
    if(total_mins != None):
        hr = total_mins // 60
        min = total_mins % 60
    else:
        total_mins = hr * 60 + min

    daytime = ""
    hr_str = ""
    min_str = ""
    if(total_mins == 0):
        return "полночь"

    elif(0 < total_mins < 6 * 60):
        daytime = "ночи"
        hr_str = str(hr) + " час" + ending(hr, 'm')
        min_str = str(min) + " минут" + ending(min, 'f')

    elif(6 * 60 <= total_mins < 12 * 60):
        daytime = "утра"
        hr_str = str(hr) + " час" + ending(hr, 'm')
        min_str = str(min) + " минут" + ending(min, 'f')

    elif(total_mins == 12 * 60):
        return "полдень"

    elif(12 * 60 < total_mins < 18 * 60):
        daytime = "дня"
        hr_clock = hr if hr == 12 else hr - 12
        hr_str = str(hr_clock) + " час" + ending(hr_clock, 'm')
        min_str = str(min) + " минут" + ending(min, 'f')

    elif(18 * 60 <= total_mins < 24 * 60):
        daytime = "вечера"
        hr_str = str(hr - 12) + " час" + ending(hr - 12, 'm')
        min_str = str(min) + " минут" + ending(min, 'f')

    else:
        return ""

    if(min == 0):
        return hr_str + " " + daytime + " ровно"

    return hr_str + " " + min_str + " " + daytime

def main():
    time_str = input().split()
    if(len(time_str) != 2):
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    try:
        hr = int(time_str[0])
        min = int(time_str[1])
    except ValueError:
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    if(not 0 <= hr <= 24):
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
        return 2

    if(not 0 <= min <= 59):
        print("Введены недопустимые данные: часы должны быть от 0 до 59")
        return 2

    print(mins_to_str(hr, min, None))
    return 0

if(__name__ == "__main__"):
    sys.exit(main())
