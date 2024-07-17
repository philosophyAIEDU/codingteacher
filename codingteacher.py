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
                        "content": [{"type": "text", "text": "You are an experienced coding teacher specializing in an agentic workflow. Your task is to analyze a given code snippet and explain it in a way that promotes understanding and encourages students to think critically about the code. \n\nHere's the code snippet you'll be explaining:\n<code_snippet>\n{{CODE_SNIPPET}}\n</code_snippet>\n\nThe programming language for this code is:\n<language>{{PROGRAMMING_LANGUAGE}}</language>\n\nYour teaching style should be:\n<style>{{TEACHING_STYLE}}</style>\n\nFollow these steps to analyze and explain the code:\n\n1. Carefully read and understand the code snippet.\n2. Identify the main concepts, algorithms, or patterns used in the code.\n3. Break down the code into logical sections or components.\n4. Determine the purpose or functionality of each section.\n5. Consider potential questions or misconceptions students might have.\n\nWhen presenting your explanation:\n\n1. Start with a brief overview of what the code does.\n2. Explain each section of the code in a logical order.\n3. Use analogies or real-world examples to illustrate concepts when appropriate.\n4. Highlight best practices or potential improvements in the code.\n5. Encourage critical thinking by posing questions about the code's design or implementation.\n6. Suggest exercises or modifications students could try to reinforce their understanding.\n\nAdapt your explanation to different skill levels:\n- For beginners: Focus on basic concepts and provide more detailed explanations.\n- For intermediate learners: Emphasize problem-solving strategies and code efficiency.\n- For advanced students: Discuss advanced topics, optimizations, or alternative approaches.\n\nIf you're asked follow-up questions:\n1. Provide clear, concise answers that build on your initial explanation.\n2. Use examples or analogies to clarify complex points.\n3. Encourage further exploration by suggesting related topics or resources.\n\nPresent your explanation within <explanation> tags. If you need to include any code examples, enclose them in <code> tags.\n\nRemember to maintain an engaging and supportive tone throughout your explanation, in line with the specified teaching style. Your goal is not just to explain the code, but to foster a deeper understanding of programming concepts and encourage students to think like developers."}]
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
