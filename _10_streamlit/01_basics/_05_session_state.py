import streamlit as st
import pandas as pd

st.title("Session State")

description = """
Streamlit은 버튼 클릭 등 사용자 상호 작용이 발생하면 스크립트(코드)를
위에서 아래로 다시 시작한다.

그래서 일반 변수에 저장된 값들이 매번 초기화 된다


Session_state를 이용하면 같은 사용자 안에서 값을 유지한다(사용자 기준 == 브라우저)
"""
st.markdown(description)

# 버튼 클릭횟수 카운트
count: int = 0
# clicked = st.button("클릭 시 count 1 증가")
# clicked

# if st.button("클릭 시 count 1 증가", key="count_key"):
# if st.button("클릭 시 count 1 증가"):
#     count += 1
# st.write(f"눌렀다리 : {count} ")


st.subheader("Session State를 이용한 count", divider=True)
# session_state
# - 서버 컴퓨터 메모리 영역에 접속한 사용자별 객체
# -> 최초 1회 접속 시에만 실행
if "count" not in st.session_state:
    # 초기화
    st.session_state["count"] = 0

if st.button("클릭 시 session_state['count'] 증가"):
    st.session_state["count"] += 1

if st.button("클릭 시 session_state['count'] 감소"):
    st.session_state["count"] -= 1

st.write(f"눌렀다리 : {st.session_state['count']} ")

