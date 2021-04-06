n = 10
a = [0]*n
print(a)

arr = []

for i in range(20):
    if i % 2 == 0:
        arr.append(i)

print(arr)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
array = []
for i in range(20):
    if i % 2 == 0:
        array.append(i)
print(array)