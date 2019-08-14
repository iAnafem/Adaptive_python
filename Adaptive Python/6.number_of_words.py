"""
Given a line, containing spaces. Find how many words are there (the word is a sequence of non-space characters,
words are separated by a single space, the first and last character of the string is not a space).

Input data

Several lines as input.

Output data

You should output the number of words in the first entered line.

Note

The find method with two arguments can be useful for this problem. The first of these is the searched substring,
the second - the position from which you should search for the first occurrence.
"""

count = 0
for i in (x for x in input().strip().split()):
    count += 1

print(count)
