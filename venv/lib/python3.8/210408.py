#
# x = 90
# if x <= 90:
#     print("90점 이하입니다..")
# elif x <= 80:
#     print("80점 미만 입니다.")
# elif x <= 70:
#     print("70점 미만 입니다.")
# else:
#     print("잘모르겠습니다")
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# remove_set = {3, 5}
# result = []
#
# for i in a:
#     if i not in remove_set:
#         result.append(i)
# print(result)
#
# b = [1, 2, 3, 4, 5, 5, 5]
#
# i = 1
# result = 0
# while i <= 9:
#     result += i
#     i += 1
# print(result)
# result = 0
# for i in range(1, 10):
#     result += i
# print(result)


scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print((i+1), "번 학생은 합격입니다.")

def add(a, b):
    print('함수의 결과', a+b)
add(3, 7)

data = list(map(int, input().split()))
