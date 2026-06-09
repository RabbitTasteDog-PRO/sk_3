import streamlit as st

# 실행 명령어

# 제목
st.title("🙇‍♂️Hello, Streamlit🙇‍")
st.header("Header", divider="rainbow")

st.subheader(":green[Sub] Header", divider=True)

# write
# - 단순 글자뿐 아니라 md,표,리스트,차트
# - 입력 방식등에 따라 출력방식이 정해짐
st.write("Write 테스트")
st.write('''
### 마크다운 먹니?
**markdown** 지원 잘되네
''')
st.write('`코드블록`')
st.markdown('### markdown')
st.write('```python\nprint("hello")\n```')
st.html('<h1>HTML <mark>도 지원한다</mark></h1>')


st.subheader(":red[magic]", divider="blue")
"streamlit magic"
"변수나 리터럴 값이 출력 구문내에 없어도 화면에 값을 기록한다"
100
lst = [1,2,3]
lst
dics = {"a":1,"b":2}
dics
########################################################################
# 소스코드
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="java", line_numbers=True)

code = '''void main()
{
    debug.log("Hello, Streamlit!");
}
'''
st.code(code, language="c#")
########################################################################
# 수식기호 : 라텍스
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 뱃지
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

st.subheader(":blue[metric]", divider="green")
st.metric(
    label="Temperature",
    value="273.15 K",
    delta="0.1 K",
    delta_color="normal",
)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

from numpy.random import default_rng as rng

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

row = st.container(horizontal=True)
with row:
    st.metric(
        "Line", 10, delta, chart_data=data, chart_type="line", border=True)
    st.metric(
        "Area", 10, delta, chart_data=data, chart_type="area", border=True
    )
    st.metric(
        "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
    )


