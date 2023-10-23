# 第1题：求离整数n最近的平方数（Find Nearest square number）
import math
def nearest_sq(n):
    sq = int(math.sqrt(n))
    if sq * sq == n:
        return n
    else:
        if (n - sq * sq) < ((sq + 1) * (sq + 1) - n):
            return sq * sq
        else:
            return (sq + 1) * (sq + 1)
    n = 111
    result = nearest_sq(n)
    print(result)
    n = 81
    result = nearest_sq(n)
    print(result)

# 第2题：弹跳的球（Bouncing Balls
def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window:
            count += 1
    return count
    h = 3
    bounce = 0.66
    window = 1.5
    result = bouncingBall(h, bounce, window)
    print(result)
    h = 3
    bounce = 1
    window = 1.5
    result = bouncingBall(h, bounce, window)
    print(result)

#第3题： 元音统计(Vowel Count)
def getCount(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

    string = "hello world"
    result = getCount(string)
    print(result)

    string = "python programming"
    result = getCount(string)
    print(result)


#第4题：偶数或者奇数（Even or Odd）

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

    result = even_or_odd(4)
    print(result)

    result = even_or_odd(7)
    print(result)
