# x = input("Введите ваше имя: ")
# y = input("Введите ваш пароль: ")
# a = input('Введите ваш возраст: ')
# print('Ваши данные для входа в аккаунт: имя - {0}, пароль - {1}, возраст - {2}'.format(x, y, a))



# x = float(input("Ведите время в секундах: "))
# seconds = x
# hours = seconds // 3600
# minutes = seconds // 60
# print("{0}:{1}:{2}".format(hours, minutes, int(seconds)))



# n = input("Введите число:  ")
# summ = int(n) + int(n + n) + int(n + n + n)
# print(summ)


# revenue = float(input("Введите сумму выручки в рублях: "))
# cost = float(input("Введите сумму издержек в рублях: "))
# result = revenue - cost
# if result < 0:
#     print("Убыток")
# elif result  > 0:
#     print("Прибыль")
#     print("Рентабельность: ", result / revenue)
# users = int(input("Введите численность пользователееп: "))
# print("Прибыль на однопользователя: ", result / users)


# from unittest import result
# def slicer(x):
#     x = str(x)
#     result = int(x[0]) + int(x[1]) + int(x[2])   
#     print(result)
    
#     return result
# while True:
#     x = input("Введите трех значное число: ")
#     if  len(x) != 3:
#         print("Числа не трехзначные")
#     else:
#         break
# slicer(x)

# j = int(input("Введите число: "))
# k = j // 3 * 2
# s = p = j // 3 // 2
# print(s, k, p)


# ticket = input("Введите номер билета: ")

# x = ticket[0:3]
# y = ticket[3:6]

# digit_sum_left  = 0
# digit_sum_right = 0

# for digit in x:
#     digit_sum_left += int(digit)
# for digit in y:
#     digit_sum_right += int(digit)
# if digit_sum_left == digit_sum_right:
#     print("Счастливый билет")
# else:
#     print("Не счастливый билет")


# n = int(input("Введите число: "))
# m = int(input("Введите число: "))
# k = int(input("Введите число: "))

# if k > n * m:
#     print("no")
# elif k % n == 0 or k % m == 0:
#     print("yes")
# else:
#     print("no")

def truncate(text, length):
    if len(text) > length:
        return text[:length]
    else:
        return text
    # END

result = truncate('hexlet', 2)

print(result + '...')