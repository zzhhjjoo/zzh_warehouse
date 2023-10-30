# 第一题 停止逆转我的单词

def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

# 第二题 发现离群的数(Find The Parity Outlier)

def find_outlier(integers):
    even_count = 0
    odd_count = 0
    even_num = None
    odd_num = None
    
    for num in integers:
        if num % 2 == 0:
            even_count += 1
            even_num = num
        else:
            odd_count += 1
            odd_num = num
            
        if even_count > 1 and odd_count == 1:
            return odd_num
        elif odd_count > 1 and even_count == 1:
            return even_num

# 第三题 检测Pangram

import string
def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Remove numbers and punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation + string.digits))
    
    # Create a set of unique characters in the sentence
    characters = set(sentence.replace(" ", ""))
    
    # Check if the set of characters is equal to the set of all lowercase letters
    return characters == set(string.ascii_lowercase)