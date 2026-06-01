# tuple
# - 변경 불가(immutable)한 리스트
# - sequence type (indexing, slicing, interable)
# - 시퀀스 타입 (순번참조, 자르기 , 반복가능)
# - 주로 함수 반환 값, 안전한 데이터 집할을 만들 떄 사용

print("--- tuple ---")
t1 = ()  # 비어있는 튜플
t2 = 10  # int로 인식됨
t3 = (10,)  # (tuple)(10) 으로 인식됨
t4 = (10, 20, 30)
t5 = 10, 20  # () 생략 -> 자동 packing , 괄호하는게 더 좋아보임
print(f"ti {t1}, type={type(t1)}")
print(f"ti {t2}, type={type(t2)}")
print(f"ti {t3}, type={type(t3)}")
print(f"ti {t4}, type={type(t4)}")
print(f"ti {t5}, type={type(t5)}")


# tuple indexing, 튜플은 읽기전용(수정불가)
tp = ("a", "b", "c", "d")
print(f"튜틀 tp[0] : {tp[0]}, tp[1] : {tp[1]}, tp[2] : {tp[2]}, tp[3] : {tp[3]},")
# tp[0] = 'A'
# print(f'튜틀 tp[0] : {tp[0]}, tp[-1] : {tp[-1]}')

# tuple slicing
print("------ tuple slicing ------")
print(f"tp[0:2] : {tp[0:2]}")  # 0번부터 2번 인덱스 미만까지 (0 , 1) : ('a', 'b')
print(f"tp[0::2] : {tp[1::2]}")  # 1번부터 끝까지 스텝은 2번째 부터 ('a', 'd')

# tupel unpacking
print("------ tuple unpacking ------")
q, w, e, r = tp
print(f"q,w,e,r : {q}, {w}, {e}, {r}")

*r, t = tp
print(f"r,t : {r}, {t}")


# tuple을 이용한 변수값 할당
print("---- tuple을 이용한 변수 값 할당 -----")
num1, num2 = (100, 200) # 표준 문법
num3, num4 = 100, 200 # 괄호 생략된 튜플

print(f"num1 : {num1}, num2 : {num2}")
print(f"num3 : {num3}, num4 : {num4}")

# tuple을 이용한 값 교환(swap)
print('------ 튜틀을 이용한 값 교환(switch) -----')
print(f"튜플을 교환 이전 // num1 : {num1}, num2 : {num2}")
num1, num2 = num2, num1
print(f"튜플을 이용한 값 교환 // num1 : {num1}, num2 : {num2}")





