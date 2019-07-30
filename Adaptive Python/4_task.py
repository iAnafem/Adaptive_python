"""
Desks

Some school have decided to create three new math groups and equip classrooms for
them with the new desks. Only two students may sit at any desk. The number of students
in each of the three groups is known. Output the smallest amount of desks, which will
need to be purchased. Each new group sits in its own classroom.

Input data format

The program receives the input of the three non-negative integers: the number of
students in each of the three classes (the numbers do not exceed 1000).
"""
print(sum((int(input()) + 1) // 2 for _ in range(3)))
