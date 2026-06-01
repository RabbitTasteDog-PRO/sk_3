# sequence type (시퀀스 자료형)
# - str , list, tuple, range
# - 저장된 값의 순서가 유지됨
# - 인덱싱과 슬라이싱이 가능함
# - 순회(interation 가능 )
from asyncio import futures
from distutils.util import copydir_run_2to3

# list
# - 여러 값(literal)을 묶어서 관리 ( 컨테이너형 자료형)
# - 특징 : 동적으로 크기 연산
print("--- list ---")
listNum = [1, 2, 3, 4, 1.5]
print(
    f"listNum : {listNum}, 길이 : {len(listNum)}, 인덱싱 = 0:{listNum[0]}, 1:{listNum[1]}, 3:{listNum[3]}"
)

# list 저장 요소 추가/수정/삭제
#  - list는 동적으로 크기 변경이 가능한 mutable(변경가능한) 자료형
# - mutable : list, set, dic => 변경 가능한
# - immutable : str, tuple, range => 변경 불가한 (메모리 새로 생성)

print("---- list mutable check ----")
print(listNum)
print("추가 전 id", id(listNum))
beforId = id(listNum)

# list.addpen ->  list.add : list.count - 1 에 값 추가
listNum.append(99999)
afterId = id(listNum)
print(f"append 후 list : {listNum}, append 후 id : {id(listNum)}")

print(
    f"appen 전후 같은 list 인가? 이전: {beforId}, 이후: {afterId} , 결과 : {beforId == afterId} "
)

# 추가
# list.insert => list.add
# - index에 값을 삽입하는 메소드
# - 지정된 index부터 한값이 밀려남
# - 모든 list 값의 index가 +1 증가 (밀려난다)
print("---- list insert() ----")
listNum.insert(2, 100)
listNum.insert(0, 0)
print("insert 후 list : ", listNum)
print("insert 후 list id : ", id(listNum))
print("insert 후 id 비교", beforId == id(listNum))


# 수정
# list.update => list[0] = value 이 개념
# list[ 인덱스 ] = 값
listNum[0] = -10
listNum[1] = 1000
print(listNum)

# 제거 : 특정 인덱스값 제거
# list.pop(index) : pop은 list 중간을 매꿈
listNum.pop(0)
# 값을 검색 해서 인덱스
index = listNum.index(1.5)
listNum.pop(index)
print(listNum)


# 2차원 배열 => [,]
student = [
    ["홍길동", 30],
    ["이순신", 80],
    ["세종대왕", 100],
]

print(student)
print(f"이름 {student[0][0]} , 점수 : {student[0][1]}")
print(student[1])
print(len(student))
print(len(student[2]))
print(len(student[2][0]))

# Split str.split('@')
data = "홍길동,20,서울시,서초구"
splitList = data.split(",")

name = splitList[0]
age = splitList[1]
addr1 = splitList[2]
addr2 = splitList[3]

print(f"splitList : {splitList}, type : {type(splitList)}")
print(f"name : {name}, age : {age}, addr1 : {addr1}, addr2 : {addr2}")

# list Slicing
print("---- list Slicing ----")
texts = ["hello", "안녕", "곤니찌와", "hi"]
print(texts[0:2])  # hello 안녕

# print(texts[1:3]) #안녕 곤니찌와
print(texts[1:3])  # 안녕 곤니찌와

# print(texts[0:3:2])# hello 곤니찌와
print(texts[0:3:2])  # hello 곤니찌와

# print(texts[2:3:1]) #곤니찌와 hi
print(texts[2:])  # 곤니찌와 hi

# slicing을 이용한 list 값 변경
print(texts)
print(texts[:2])
texts[:2] = ["aaa", "bbb"]
print(texts)

texts[1:3:1] = ["🌚🌚🌚", "❄️❄️❄️"]
print(texts)

# list 더하기 연산
print("----- list 더히기 연산 -----")
a = [10, 20]
b = [30, 40]
a = a + b
print(a)

b = b + a
print(b)

# list 순회
# - iterable 특징을 가지는 자료형만 가능
print("----- list 순회 -----")
lst = ["a", "b", "c"]

# list 요소 순회
for v in lst:
    print(v)

for i in range(len(lst)):
    print(f"lan  // {i} : {lst[i]}")

for index, v in enumerate(lst):
    print(f"enumerate // {index} : {v}")


# list api

# list count , 리스트 안에 같은값이 몇개 있는가 :  linq => list.count(x => x == true)
print("----- list.count -----")
fruits = ["apple", "banana", "apple", "orange", "banana"]
print("사과 몇개? :", fruits.count("apple"))
print("바나나 몇개? : ", fruits.count("banana"))
print("키위 몇개? : ", fruits.count("kiwi"))

# 정렬 sort : list.sort
# list.sort() : 원본 리스트 내에서 정렬 (in-place) 원본이 변경됨
# sorted(list) : 정렬된 새 리스트를 반환함 (not-in-place)

# list.sort(0,1) <- 이렇게 오더되는것
#
print("----- list.sort -----")
nums = [100, 240, 130, 4, 50]
nums.sort()
print(f"오름차순 : {nums}")
# 이건안된 return 값이 없어서 none나옴
print(f"오름차순 : {nums.sort()}")
nums.sort(reverse=True)
print(f"내림차순 : {nums}")

# key 속성 -> 정렬 기준 함수
print("----- key 속성 -> 정렬 기준 함수 -----")
fruits.append("kiwi")
print(f"fruits : {fruits}")
fruits.sort(key=len)  # <- 함수로 넣어도 될듯?
print(f"len으로 정렬된 fruits : {fruits}")


# 커스텀 정렬기준함수
def my_sort(elem):
    return len(elem), elem  # tuple로 우선순위 지정


fruits.sort(key=my_sort)
print("커스텀 정렬 함수 :", fruits)


# sorted() : 원본 유지 정렬 (새 리스트 반환)
print("------ sorted(list) ------")
nums = [9,2,4,7,1]
nums2 = sorted(nums)
print(nums, id(nums))
print(nums2, id(nums2))

# list unpacking(묶음 풀기)
# *** 이건 강려크 한것같다
#- list == 변수의 묶음
print('------ list unpacking -----')
numbers = [10,20,30]
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# unpacking기능은 편하넹
a,b,c = numbers
print(a,b,c);

# d에는 0번 인텍스 요소
# *e는 나머지 요소들, 변수로 안되니까 [20,30]이 들어감
d,*e = numbers
print(f"d(0번째요소) : {d}, *e(나머지) : {e}")

numbers = [10,20,30,40,50]
a, *b, c = numbers
print(f"a : {a}, b : {b}, c : {c}")


