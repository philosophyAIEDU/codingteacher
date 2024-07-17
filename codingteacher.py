import streamlit as st
import anthropic
import os

# Streamlit 앱 제목 설정
st.title("Anthropic API Streamlit 코딩티쳐")

# 사이드바에 API 키 입력 필드 추가
api_key = st.sidebar.text_input("Anthropic API 키를 입력하세요", type="password")

# 메인 영역에 사용자 입력 필드 추가
user_input = st.text_area("메시지를 입력하세요", height=100)

# 전송 버튼 추가
if st.button("전송"):
    if api_key and user_input:
        try:
            # Anthropic 클라이언트 초기화
            client = anthropic.Anthropic(api_key=api_key)

            # 메시지 생성
            message = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1000,
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": user_input}]
                    }
                ]
            )

            # 응답 표시 (텍스트 내용만 추출)
            st.write("Claude의 응답:")
            st.write(message.content[0].text)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
    else:
        st.warning("API 키와 메시지를 모두 입력해주세요.")