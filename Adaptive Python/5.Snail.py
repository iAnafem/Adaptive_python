"""
Snail

Snail creeps up the vertical pole of height H feets. Per day it goes A feets up, and per night it goes B feet down.
In which day the snail will reach the top of the pole?

Input data format

On the input the program receives non-negative integers H, A, B, where H > B and A > B.
Every integer does not exceed 100.

Sample Input:

10
3
2
Sample Output:

8
"""
from math import ceil

h, a, b = (num for num in (int(input()) for i in range(3)))
print(ceil((h - b) / (a - b)))
