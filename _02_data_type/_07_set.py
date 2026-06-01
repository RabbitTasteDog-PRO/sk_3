# set 집합
# 중복 허용 안됨
# 시퀀스 타입이 아님
# 단 순회타입은 됨 자료구조라 되는것 같음
# 집합 관렴 메소드 제공

print("--- set ---")
st = {1, 2, 4, 6, 7, 3, 4, 6, 3, 6, 5, 4, 2, 3, 5}
# 로그만 정렬됨, 실제로는 정렬은 보장안됨
# 중복저거된것은 확인
print(f"set : {st}, type : {type(st)}")

# list to set
print("------ list to set 변경")
lst = [1, 2, 4, 6, 7, 2, 3, 9, 4, 2]
# set으로 변환 컨버트 없이 자동으로 지원 되나봄?
st2 = set(lst)
print(f"set2 : {st2}, type : {type(st2)}")

# set to list
# 이건 개꿀이넹
print("------ set to list 변경 ------")
lst2 = list(st2)
print(f"list2[3] : {lst2[3]}, type : {type(lst2)}")

print("---- tupple to set 변경 -----")
tpl = (1, 2, 4, 6, 7, 2, 3, 9, 4, 2)
st3 = set(tpl)
print(f"set3 : {st3}, type : {type(st3)}")

# set 요소 추가 add
print("---- set 요소 추가 (add)-----")
myNums = {20, 30, 40}
print(f"myNums 이전 : {myNums}")
myNums.add(50)
myNums.add(50)  # 중복 안되서 하나만 들어감
myNums.add(50)
print(f"myNums 추가 : {myNums}")

# set 요소 제거 remove
print("---- set 요소 제거 -----")
myNums.remove(50)
print(f"myNums remove : {myNums}")


# set clear
print("---- set Clear -----")
myNums.clear()
print(f"myNums clear : {myNums}")


# set 순회
print("---- set 순회 -----")
myNums = {20, 30, 40, 100, 458, 299}
for v in myNums:
    print(v)

# # 이건 인덱싱이 안되서 해당 안됨
# for v in len(myNums):
#     print(v)


# 집합연산 (교집합, 차입합)
print("---- 집합연산 (교집합, 차입합) -----")
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합
