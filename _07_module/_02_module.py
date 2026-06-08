"""
# 모듈이란
- .py 파일을 의미
- 프로그램 내 코드 재사용성을 높이기 위해 모듈 단위로 코드를 관리
- 모듈에 작성 된 변수, 함수, 클래스 등은 외부에서 import해 사용 가능
- 단, _,__ 시작하는 이름은 "내부용":Private 이라는 관례가 있음
  -> 외부에서 import 해서 사용하는 것을 지양함

- import * -> 모듈 내 모든 변수, 함수, 클래스를 가져옴
           -> 단, _,__ 시작하는 변수, 함수, 클래스들은 자동 제외
"""

# 파이썬 내장 모듈 math 가져오기
import math

print(math.pi)

# dir(모듈명) 내장 함수 : 해당 모듈의 사용 가능한 속성/함수 등을 나열
print(dir(math))
# dir() 내장 함수 : 현재 모듈(_02_module.py)의 사용 가능한 속성/함수 등을 나열
print(f"dir() : {dir()}" )

# 모듈명 확인
print(f"__name__ : {__name__}")
print(f"math.__name__ : {math.__name__}")

print('-'*50)

""" 사용자 정의 모듈 가져오기 """
# import skn.my_math
# print(f"skn.my_math.pi : {skn.my_math.pi}")
""" 파이썬 패키지로 모듈 가져오기 """
# from skn import my_math
# print(f"my_math.pi : {my_math.pi}")
# print(f"my_math.x : {my_math.x}")
# print(f"my_math.get_circle_area(2) : {my_math.get_circle_area(10)}")
# print(f'__z : {my_math.__z}') # private 변수를 가져오는것은 권장하지 않는다

# import * 모두 가져오기
from skn.my_math import *
print(f"pi : {pi}")
print(f"x : {x}")
print(f"get_circle_area(2) : {get_circle_area(10)}")
# print(f"__z : {__z}") <- 못가져온다


""" import 모듈 별칭 처리"""
# import 모듈명 / import 패키지명.모듈명 : 지정된 모듈 가져오기
# 사용법 -> 모듈명.변수명 / 패키지명.모듈명.변수명

# from 패키지명 import 모듈명 : 지정된 패키지에서 모듈 가져오기
# 사용법 -> 모듈명.변수명

# import 모듈명 as 별칭
# from 패키지명 import 모듈명 as 별칭

from skn import my_math as mm
print(f"mm.pi : {mm.pi}")
print(f"mm.x : {mm.x}")
print(f"mm.get_circle_area(2) : {mm.get_circle_area(10)}")
"""
import * 을 이용해서 가져오는 것 보다 
import 모듈명, import 모듈명 as 별칭 사용법을 권장한다
출동 방지 및 가독성 용으로 권장됨
"""

# __name__: 현재 모듈의 이름을 반환
print(f"__name__ : {__name__}")

# 현재 모듈을 import해서 사용하는 경우 하위 코드를 실행하지 마시오
if __name__ == '__main__':
    pass # continue 같은?

