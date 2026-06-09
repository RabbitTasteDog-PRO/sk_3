import streamlit as st
import pandas as pd

st.title("Input Widgets")
st.header("Button", divider=True)

clicked = st.button("Click Me", width="content")

print("clicked :", clicked)

if clicked:
    st.write("버튼 선택")
else:
    st.write("아직 버튼을 클릭하지 않았습니다.")
print(clicked)

st.button("Reset", type="primary")

st.header("Button 샘플", divider=True)
left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")

st.header("text_input 테스트 ", divider=True)
title = st.text_input(label="가고싶은 여행지가 있으신가요?", placeholder="여행지를 입력하세요")
st.write("입력된 여행지 : ", title)

st.header("text_area 테스트 ", divider=True)

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)
st.write(f"You wrote {len(txt)} characters.")

# 여러개중 한가지만
st.header("라디오 버튼 샘플", divider=True)
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

st.header("셀렉트박스 샘플", divider=True)
st.header('SelectBox')
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    # index=보여줄번호
    index=2
)
if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')

st.header("체크박스 샘플", divider=True)
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
