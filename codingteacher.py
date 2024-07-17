import streamlit as st
import anthropic

# Streamlit 앱 제목 설정
st.title("초보자를 위한 한국어 코딩 교육 AI")

# API 키 입력
api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")

if not api_key:
    st.warning("Anthropic API 키를 입력해주세요.")
    st.stop()

# Anthropic 클라이언트 초기화
client = anthropic.Anthropic(api_key=api_key)

# 사용자 입력
name = st.text_input("이름을 알려주세요:")
experience = st.radio("코딩 경험이 있나요?", ["전혀 없음", "조금 있음", "어느 정도 있음"])
interests = st.text_area("어떤 분야의 코딩에 관심이 있나요?")

# 학습 시작 버튼
if st.button("학습 시작"):
    if name and interests:
        try:
            prompt = f"당신은 한국어 코딩 교육 AI입니다. 다음 학습자에 대해 응답해주세요: 이름: {name}, 코딩 경험: {experience}, 관심 분야: {interests}. 학습자를 환영하고, 그들의 관심사에 맞는 간단한 코딩 개념을 소개해주세요."
            
            response = client.completions.create(
                model="claude-2.1",
                max_tokens_to_sample=1000,
                temperature=0.5,
                prompt=prompt
            )
            
            st.write("AI 교사의 응답:")
            st.write(response.completion)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
    else:
        st.warning("이름과 관심 분야를 모두 입력해주세요.")
