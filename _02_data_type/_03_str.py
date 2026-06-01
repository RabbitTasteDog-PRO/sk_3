# str 문자형, 문자열, string
# - "",'', """ 감싸서 표현 """, ''' 감싸서 표현  ''',

print("----strt----")
print("--- 홑 따옴표, 쌍 따옴표 ")
s1 = "Hello"
s2 = "World"
s3 = "'abc'"

print(f"{s1} {s2} // type s1 : {type(s1)} ,s2: {type(s2)}, ")
print(s3)

# 삼중따옴표
print("""
길게 쓸때는 이게 좋네용
플러스 없는것도 좋네용
""")

print("""앞/뒤 공백없이 사용하면
한줄로 나오네용 이것도 좋은것 같네용""")
"""
/*
 이것과 강튼 개념이네용
*/
"""
print("--------- 문자열 이어쓰기 ---------")
# str 연산
# 1. 문자열 + 문자열 = 이어쓰기
apple = "사과"
banana = "바나나"
print(apple + banana)
# 2. 문자열 * 양의 정수 = 양의 중수 크기만큼 반복
print("문자열 " * 3)

# len(객체): 파이썬 객체의 길이 반환 char
print("----len()-----")
text = "오늘 점심은 뭘먹지"
print(len(text))

# srt.replace(old, new)
# 리플레이스 기능 동일
print("-----srt replace-----")
today = "2026-06-01"
print(today, today.replace("-", "/"))

# str.strip() => Trim()
# 앞뒤 공백만 제거
print("-----str.strip()-----")
some = (
    "공백제 거공백제 거공백제  거공백 제 거공백제거공백  제거공백제거 공백제 거      "
)
print("[" + some + "]")
print("앞뒤 공백 제거 : [" + some.strip() + "]")
print("모든 공백 제거 : [" + some.replace(" ", "") + "]")


# 대소문자 관련 메소드
origin_str = "hELLO wORLD!"
# upper() : 대문자로 변경한다.
print(origin_str.upper())  # HELLO WORLD!
# lower() : 소문자로 변경한다.
print(origin_str.lower())  # hello world!
# capitalize() : 첫 글자만 대문자로 변경한다.
print(origin_str.capitalize())  # Hello world!
# swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경한다.
print(origin_str.swapcase())  # Hello World!
# title() : 단어의 첫글자를 대문자로 변경한다. (띄어쓰기 일을경우)
print(origin_str.title())  # Hello World!

#str.format : 동일하게 사용하긴 하는데 여긴 숫자가 없네?
print("-----str.format-----")
print("{} {} {}".format(1,2,3))

# f-string : 에프스트링이라고 파이썬은 명명하네?
print("-----f-string-----")
print(f"{s1} {s2} // type s1 : {type(s1)} ,s2: {type(s2)}, ")
# ************************************************************************************
# 텍스트 인덱싱/슬라이싱
# - 파이썬 문자열(str)은 text sequence 형태를 갖는다




# ************************************************************************************



# str 메소드 (str api)
def print_hello():
    hello = "Hello"
