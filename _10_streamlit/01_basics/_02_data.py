import streamlit as st
import pandas as pd

# pandas란?
# - 데이터 분석과 조작을 위해 설계된 파이썬 라이브러리
# - 특히, 구조화된 데이터(표형식) 처리에 특화
# - DataFrame이라는 구조를 중심으로 빠르고 직관적인
#   데이터 처리 및 분석을 지원한다


st.title("Data Pandas")
st.header("Pandas 'DataFrame'을 알아보자", divider=True)
student_df = pd.DataFrame({
    'Name': ['홍길동', '이순신','신사임당'],
    'Age': [20,30,40],
    'Score': [90,88,77]
})

st.dataframe(student_df)

st.header("DataFrame + csv", divider='green')
sample_csv = pd.read_csv("../Data/annual-enterprise-survey-2023.csv")
st.dataframe(sample_csv)


st.header("DataFrame 강조 기능", divider='yellow' )
data = {
    "Product":["A","B","C","D"],
    "Sales":[500,300,400,600],
    "Growth(%)":[10,-5,10,4]
}

# DataFrame 객체 생성
df = pd.DataFrame(data)
# 시각적 강조
st.dataframe(
    df.style
        # 최대치
        .highlight_max(subset=["Sales"], color="lightgreen")
        # 최소치
        .highlight_min(subset=["Growth(%)"], color="red")
)

# 열 설정 추가
# 열 설정을 추가한 DataFrame 표시
st.dataframe(df, column_config={
    "Sales": st.column_config.NumberColumn("Total Sales", format="%d units"),
    "Growth(%)": st.column_config.NumberColumn("Growth Percentage", format="%.1f%%")
}, width="stretch")
