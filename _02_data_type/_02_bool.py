# 논리형 Boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

# 비교 연산
# A > B : A가 B 보다 크면 True, 아니면 False
# A >= B : A가 B 이상이면 True, 아니면 False
# A < B
# A <= B
# A == B : A, B가 같으면 True, 아니면 False
# A != B : A, B가 같지 않으면 True

print("1 > 0.5:", 1 > 0.5)    # True
print("1 < 0.5:", 1 < 0.5)    # False
print("1 >= 0.5:", 1 >= 0.5)  # True
print("1 <= 0.5:", 1 <= 0.5)  # False
print("1 == 1:", 1 == 1)      # True
print("1 != 1:", 1 != 1)      # False

# 논리 부정 연산(not)
print(True)
print(not True)
print(not not True)




# 60점 이상 입력시  합격(true) 아니면 불합격(flase)
print("--- 합격/불합격 ---")
# score = int(input("점수를 입력하세요 : "))
score = input("점수를 입력하세요 : ")
print(score, type(score))
result = int(score) >= 60
# print(f"점수 : {score} , 합격 : {result}")
print("합격 여부 : " , '합격' if result == True else '불합격')

