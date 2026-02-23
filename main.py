# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i * 3
print(s)

# 2
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i - 1
print(s)

# 3
n = int(input())
p = 1
for i in range(1, n + 1):
    p *= (i + 1)
print(p)

# 4
n = int(input())
c = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        c += 1
print(c)

# 5
n = int(input())
for i in range(1, n + 1):
    print(i, i * 2)
