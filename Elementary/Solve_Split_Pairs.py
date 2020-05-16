"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Precondition: 0<=len(str)<=100
"""

def split_pairs(a):
    answer = []
    if len(a) % 2 == 1:
        a += "_"
    if len(a) % 2 == 0:
        for i in range(0,len(a),2):
            answer.append(a[i:i+2])
        return answer


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""
Recursive Solution

def split_pairs(a):
    l = len(a)
    if l == 0:
        return []
    if l == 1:
        return [a + '_']
    else:
        return [a[:2]] + split_pairs(a[2:])
"""

"""
Optimized Solution

def split_pairs(a):
    if len(a) % 2:
        a += '_'
    return [a[i:i+2] for i in range(0, len(a), 2)]
    
"""