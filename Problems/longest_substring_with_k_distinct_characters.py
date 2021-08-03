'''
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
'''
def longest_substring_with_k_distinct_characters(s, k):
    window_start = 0
    freq = {}
    max_len = 0
    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] = 0
        freq[s[i]] += 1
        while len(freq) > k:
            freq[s[window_start]] -= 1
            if freq[s[window_start]] == 0:
                del freq[s[window_start]]
            window_start += 1
        max_len = max(max_len,i - window_start +1)
    return max_len
if __name__ == '__main__':

    print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
    # 5 (because 'defff' has length 5 with 3 characters)