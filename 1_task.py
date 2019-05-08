A, B, N = [a for a in (int(input()) for i in range(3))]
print(*[A*N + B*N // 100, B*N % 100])
