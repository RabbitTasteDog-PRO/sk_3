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
# print("길이를 나타냅니다 : " + len(text))
# 이렇겐 안되고 파이썬은 무조건 형변환 해야함
print("길이를 나타냅니다 : " + str(len(text)))

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

# str.format : 동일하게 사용하긴 하는데 여긴 숫자가 없네?
print("-----str.format-----")
print("{} {} {}".format(1, 2, 3))

# f-string : 에프스트링이라고 파이썬은 명명하네?
print("-----f-string-----")
print(f"{s1} {s2} // type s1 : {type(s1)} ,s2: {type(s2)}, ")
# ************************************************************************************
# 텍스트 인덱싱/슬라이싱
# - 파이썬 문자열(str)은 text sequence 형태를 갖는다
print("--- 정인덱스 ---")
x = "Monday"
print(f"len {len(x)} ")
print(f"len {x[0]} ")
print(f"len {x[1]} ")
print(f"len {x[2]} ")
print(f"len {x[3]} ")
print(f"len {x[4]} ")

# -1은 가장 뒤부터 문법이 왜 이따위지?
print("--- 역 인덱스 ---")
print(f"len {x[-1]} ")
print(f"len {x[-2]} ")
print(f"len {x[-3]} ")
print(f"len {x[-4]} ")
print(f"len {x[-5]} ")
print(f"len {x[-6]} ")

# 슬라이싱 : 문자열 일부를 가져오는 방법 Substring
# str.[시작인덱스(0 + 1):종료인덱스(미포함):스텝(건너뛸 개수 , 생략 시 기본값 1)]
print("--- str slicing ---")
text = "Hello World"
print(f"text 기본 : {text} ")
print(f"text 길이: {len(text)} ")
print(f"text slicing [1:3]: {text[1:3]} ")  # el
print(f"text slicing [1:]: {text[1:]} ")  # 시작부터 끝까지  ello World
print(f"text slicing [:3]: {text[:3]} ")  # Hel
print(f"text slicing [1:3:2]: {text[1:3:2]} ")  # e
print(f"text slicing [::2]: {text[::2]} ")  # HloWrd (0,2,4,8,10) 이렇게 나옴
print(f"text slicing [::-1]: {text[::-1]} ")  # dlroW olleH : 뒤로 나오게
print(f"text slicing [::len(text)]: {text[: len(text)]} ")

# ************************************************************************************
# 문자열 불변타입 (immutable)
# - 불변타입 : 메모리에 한번 저장된것은 수정할수없다
# - 메모리상 문자열의 크기를 지정할수없다
# - 새로운 문자열을 생성할때마다 메모리에 생성 및 만들고 이전 메모리는 삭제 한다
print("---- 문자열 불변타입 ----")
s = "python"  # s에는 'python' str 메모리 주소가 저장됨
print(s)  # s에 저장된 주소를 찾아가서 'python' str을 참조
print(f"text : {s}, 변경전 s {id(s)}")
s = s + " hello"  # 기존 문자열의 주소는 삭제되고 새롭게 메모리 생성
print(f"text : {s}, 변경후 s {id(s)}")

# ************************************************************************************
# in 연산자(맴버쉽 검사)
# 특정값이 포함되어있는지 검사  : contains
# 결과는 동일하게 bool T/F

print('---- in 연산자(맴버쉽 검사) ----')
txt = "김밥, 라면, 어묵, 떡뽁이"
print('라면 : ' in txt + ', 돈끼스 : ' in txt)
print(f"txt : {txt}, 김밥 포함여부 : {'김밥' in txt}")

