# 6055
# a, b = map(int, input().split(' '))
# print(bool(a or b == 1))

# 6056
# a, b = map(int, input().split(' '))
# print(bool(a!=b))

# 6057
# a, b = map(int, input().split(' '))
# print(bool(a == b))

# 6058
# a, b = map(int, input().split(' '))
# print(bool(a == 0 and b == 0))

# # 6059
# n = int(input())
# print(~n)

# 6060
# n, m = map(int, input().split())
# print(n & m)

# 6061
# a, b = map(int, input().split(' '))
# print(a | b)

# 6062
# a, b = map(int, input().split(' ')) # 서로 다를 때만 1이다.
# print(a ^ b)

# # 6063
# a, b = map(int, input().split(' '))
# c = (a if (a>=b) else b)
# print(c)

# 6064
a, b, c = map(int, input().split(' '))
d = (a if a<b else b) if ((a if a<b else b) < c) else c
print(d)