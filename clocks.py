#!/usr/bin/python
import sys

def ending(number, type):
    if(type != "m" and type != "f"):
        return "err"

    number = abs(number)
    if(number % 10 > 4 or number % 10 == 0 or 10 < number % 100 < 20):
        return "ов" if type == 'm' else ""
    elif(number % 10 == 1):
        return "" if type == 'm' else "а"
    else:
        return "а" if type == 'm' else "ы"

def time_to_str(hours, minute, total_minutes):
    if(total_minutes != None):
        hours = total_minutes // 60
        minute = total_minutes % 60
    else:
        total_minutes = hours * 60 + minute

    daytime = ""
    hours_str = ""
    minutes_str = ""
    if(total_minutes == 0):
        return "полночь"

    elif(0 < total_minutes < 6 * 60):
        daytime = "ночи"
        hours_str = str(hours) + " час" + ending(hours, 'm')
        minutes_str = str(minutes) + " минут" + ending(minute, 'f')

    elif(6 * 60 <= total_minutes < 12 * 60):
        daytime = "утра"
        hours_str = str(hours) + " час" + ending(hours, 'm')
        minutes_str = str(minutes) + " минут" + ending(minute, 'f')

    elif(total_minutes == 12 * 60):
        return "полдень"

    elif(12 * 60 < total_minutes < 18 * 60):
        daytime = "дня"
        hours_clock = hours if hours == 12 else hours - 12
        hours_str = str(hours_clock) + " час" + ending(hours_clock, 'm')
        minutes_str = str(minutes) + " минут" + ending(minute, 'f')

    elif(18 * 60 <= total_minutes < 24 * 60):
        daytime = "вечера"
        hours_str = str(hours - 12) + " час" + ending(hours - 12, 'm')
        minutes_str = str(minutes) + " минут" + ending(minute, 'f')

    else:
        return ""

    if(minute == 0):
        return hours_str + " " + daytime + " ровно"

    return hours_str + " " + minutes_str + " " + daytime

def main():
    time_str = input().split()
    if(time_str == [] or time_str[0] == "help"):
        print("Требуется ввести время в формате xx yy где xx от 0 до 23 и yy от 0 до 59.")
        return 2
    if(len(time_str) != 2):
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    try:
        hours = int(time_str[0])
        minute = int(time_str[1])
    except ValueError:
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    if(not 0 <= hours < 24):
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
        return 2

    if(not 0 <= minutes < 60):
        print("Введены недопустимые данные: часы должны быть от 0 до 59")
        return 2

    print(time_to_str(hours, minute, None))
    return 0

if(__name__ == "__main__"):
    sys.exit(main())

