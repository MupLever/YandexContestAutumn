"""
Дан массив строк, необходимо сгруппировать анаграммы.
Слово X является анаграммой слова Y, если одно может быть получено
из другого перестановкой букв.
В итоговом массиве каждый массив анаграмм должен быть отсортирован в
лексикографическом порядке.
Все слова в исходном массиве состоят только из строчных латинских букв

Sample Input:
["eat", "tea", "and", "ate", "nat", "bat"]

Sample Output 
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
"""

from collections import defaultdict

def subarrays_anagram(array):
    sub_array_dict = defaultdict(list)
    for s in array:
        sub_array_dict[''.join(sorted(s))].append(s)

    for k in sub_array_dict:
        sub_array_dict[k].sort()
    return list(sub_array_dict.values())
