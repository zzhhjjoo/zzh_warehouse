#第一题：3和5的倍数（Multiples of 3 or 5）
def solution(number):
    if number < 0:
        return 0
    else:
        result = 0
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                result += i
        return result

#第二题： 重复字符的编码器（Duplicate Encoder）
def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for char in word:
        if word.count(char) == 1:
            new_word += "("
        else:
            new_word += ")"
    return new_word

#第三题：括号匹配（Valid Braces）
def valid_braces(string):
    stack = []
    braces = {'(': ')', '[': ']', '{': '}'}
    for char in string:
        if char in braces.keys():
            stack.append(char)
        elif char in braces.values():
            if len(stack) == 0 or braces[stack.pop()] != char:
                return False
    return len(stack) == 0

#第五题： 去掉喷子的元音（Disemvowel Trolls）

def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string