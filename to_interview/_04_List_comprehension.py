a = [[x, y ** 2] if y % 2 == 0 else [x, y ** 3] for x in range(5) for y in range(15, 20)]
print(a)
