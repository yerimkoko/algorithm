array = [1,2,3]

array.append(4) # 배열에 추가
print(array)



array.sort(reverse = True)
print(array)

array.sort()
print(array)

array.reverse()
print(array)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
# a에 포함된 원소를 하나씩 확인하며 그 원소가 remove_set에 포함되어 있지 않았을 때만 리스트 변수인 result에 넣겠다는 의미이다.
result = [i for i in a if i not in remove_set]
print(result)

# 문자열 자료형
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = 'Hello'
b = 'world'
print(a + " " + b)

# 튜플 자료형
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호([])를 이용하지만 튜플은 소괄호({})를 이용한다.

# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = "banana"
# data['코코넛'] = 'Coconut'
# print(data)
#
# if '사과' in data:
#     print("'사과'를 가지는 데이터가 없습니다.")

# 집합 자료형 초기화 방법 I.
data = set([1,2,3,4,4,5]) # set을 이용해 세팅을 한다.
print(data)

# 집합 자료형 초기화 방법 II.
data = {1, 2, 3, 4, 4, 5}
print(data)


a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

data = set([1, 2, 3])
print(data)
제
data.add(4) # 집합 자료형에 새로운 원소 추가
print(data)

data.update([5,6]) # 새로운 원소 여러 개 추가.
print(data)

data.remove(3) # 특정한 값을 갖는 원소 삭
print(data)
# # 집합 자료형 초기화 방법 1
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
# print(data)
#
# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")
#
# a = set([1, 2, 3, 4, 5])
#
# b = set([3, 4, 5, 6, 7])
#
#
# # 합집합
# print(a | b)
#
# # 교집합
# print(a & b)
#
# # 차집합
# print(a - b)
#
# data = set([1, 2, 3])
# print(data)
#
#
# # 새로운 원소 추가
# # dataList.add(4)
# # print(data)
# #
# # 새로운 원소 여러 개 추가
# # dataList.update([5, 6])
# # print(data)
#
# # 원소 제거
# # dataList.remove(3)
# # print(data)
