
# 第二题 使用函数进行计算
def zero(operation=None):
    if operation:
        return operation(0)
    return 0

def one(operation=None):
    if operation:
        return operation(1)
    return 1

def two(operation=None):
    if operation:
        return operation(2)
    return 2

def three(operation=None):
    if operation:
        return operation(3)
    return 3

def four(operation=None):
    if operation:
        return operation(4)
    return 4

def five(operation=None):
    if operation:
        return operation(5)
    return 5

def six(operation=None):
    if operation:
        return operation(6)
    return 6

def seven(operation=None):
    if operation:
        return operation(7)
    return 7

def eight(operation=None):
    if operation:
        return operation(8)
    return 8

def nine(operation=None):
    if operation:
        return operation(9)
    return 9

def plus(x):
    return lambda y: x + y

def minus(x):
    return lambda y: x - y

def times(x):
    return lambda y: x * y

def divided_by(x):
    return lambda y: x // y

# 第三题 缩短数值的过滤器(Number Shortening Filter)
import math

def shorten_number(suffixes, base):
    def filter_number(num):
        if isinstance(num, str) and num.isdigit():
            num = int(num)
            power = 0
            while math.isclose(num, base, rel_tol=1e-09) or num >= base:
                num /= base
                power += 1
            if power < len(suffixes):
                return f"{num}{suffixes[power]}"
            else:
                return str(num)
        return str(num)
    return filter_number


# 第四题 编码聚会7

def find_senior(lst):
    max_age = max(dev['age'] for dev in lst)
    return [dev for dev in lst if dev['age'] == max_age]
