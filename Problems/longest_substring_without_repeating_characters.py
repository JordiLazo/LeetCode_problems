'''
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(string):
    seen = {}
    maximum_lenght = 0
    start = 0

    for end in range(len(string)):
        if string[end] in seen:
            start = max(start,seen[string[end]] +1 )
        seen[string[end]] = end
        maximum_lenght = max(maximum_lenght, end-start +1)

    return maximum_lenght


def findLongestSubstring(string):
    n = len(string)
    # starting point of current substring.
    st = 0
    # maximum length substring without
    # repeating characters.
    maxlen = 0
    # starting index of maximum
    # length substring.
    start = 0

    # Hash Map to store last occurrence
    # of each already visited character.
    pos = {}

    # Last occurrence of first
    # character is index 0
    pos[string[0]] = 0

    for i in range(1, n):

        # If this character is not present in hash,
        # then this is first occurrence of this
        # character, store this in hash.
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            # If this character is present in hash then
            # this character has previous occurrence,
            # check if that occurrence is before or after
            # starting point of current substring.
            if pos[string[i]] >= st:

                # find length of current substring and
                # update maxlen and start accordingly.
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st

                # Next substring will start after the last
                # occurrence of current character to avoid
                # its repetition.
                st = pos[string[i]] + 1

            # Update last occurrence of
            # current character.
            pos[string[i]] = i

    # Compare length of last substring with maxlen
    # and update maxlen and start accordingly.
    if maxlen < i - st:
        maxlen = i - st
        start = st

    # The required longest substring without
    # repeating characters is from string[start]
    # to string[start+maxlen-1].
    return string[start: start + maxlen]

if __name__ == '__main__':
    string = "abrkaabcdefghijjxxx"
    print("The input string is:", string)
    print("The length of the longest non-repeating character substring is:", lengthOfLongestSubstring(string))
    print("The substring with the longest non-repeating character is:",findLongestSubstring(string))