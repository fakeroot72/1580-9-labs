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

def time_to_str(hour, minute, total_minutes):
    if(total_minutes != None):
        hour = total_minutes // 60
        minute = total_minutes % 60
    else:
        total_minutes = hour * 60 + minute

    daytime = ""
    hour_str = ""
    minutes_str = ""
    if(total_minutes == 0):
        return "полночь"

    elif(0 < total_minutes < 6 * 60):
        daytime = "ночи"
        hour_str = str(hour) + " час" + ending(hour, 'm')
        minutes_str = str(minute) + " минут" + ending(minute, 'f')

    elif(6 * 60 <= total_minutes < 12 * 60):
        daytime = "утра"
        hour_str = str(hour) + " час" + ending(hour, 'm')
        minutes_str = str(minute) + " минут" + ending(minute, 'f')

    elif(total_minutes == 12 * 60):
        return "полдень"

    elif(12 * 60 < total_minutes < 18 * 60):
        daytime = "дня"
        hour_clock = hour if hour == 12 else hour - 12
        hour_str = str(hour_clock) + " час" + ending(hour_clock, 'm')
        minutes_str = str(minute) + " минут" + ending(minute, 'f')

    elif(18 * 60 <= total_minutes < 24 * 60):
        daytime = "вечера"
        hour_str = str(hour - 12) + " час" + ending(hour - 12, 'm')
        minutes_str = str(minute) + " минут" + ending(minute, 'f')

    else:
        return ""

    if(minute == 0):
        return hour_str + " " + daytime + " ровно"

    return hour_str + " " + minutes_str + " " + daytime

def main():
    time_str = input().split()
    if(time_str == [] or time_str[0] == "help"):
        print("Требуется ввести время в формате xx yy где xx от 0 до 23 и yy от 0 до 59.")
        return 2
    if(len(time_str) != 2):
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    hour = 0
    minute = 0

    try:
        hour = int(time_str[0])
        minute = int(time_str[1])
    except ValueError:
        print("Введены недопустимые данные: присутствуют посторонние символы")
        return 2

    if(not 0 <= hour < 24):
        print("Введены недопустимые данные: часы должны быть от 0 до 23")
        return 2

    if(not 0 <= minute < 60):
        print("Введены недопустимые данные: часы должны быть от 0 до 59")
        return 2

    print(time_to_str(hour, minute, None))
    return 0

if(__name__ == "__main__"):
    sys.exit(main())

