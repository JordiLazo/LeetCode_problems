'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
'''
from collections import defaultdict


def groupAnagrams(strs):
    lookup = defaultdict(list)

    for s in strs:
        key = "".join(sorted(list(s)))
        lookup[key].append(s)

    output = []
    for l in lookup.values():
        output.append(l)
    return output



if __name__ == '__main__':
    print(groupAnagrams(['abc', 'bcd', 'cba', 'cbd', 'efg']))
    # [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]