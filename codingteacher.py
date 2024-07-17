import streamlit as st
import anthropic

# Streamlit 앱 제목 설정
st.title("코딩 교사 AI - Anthropic API 활용")

# 세션 상태 초기화
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

# API 키 입력 섹션
st.header("API 키 설정")
api_key_input = st.text_input("Anthropic API 키를 입력하세요:", type="password", value=st.session_state.api_key)

if st.button("API 키 저장"):
    st.session_state.api_key = api_key_input
    st.success("API 키가 저장되었습니다!")

# API 키 확인
if not st.session_state.api_key:
    st.warning("Anthropic API 키를 입력해주세요.")
    st.stop()

# Anthropic 클라이언트 초기화
client = anthropic.Anthropic(api_key=st.session_state.api_key)

# 코드 스니펫 입력
st.header("코드 분석")
code_snippet = st.text_area("설명할 코드 스니펫을 입력하세요:", height=200)
programming_language = st.text_input("프로그래밍 언어를 입력하세요:")
teaching_style = st.selectbox("교육 스타일을 선택하세요:", ["친근한", "전문적인", "유머러스한"])

# 전송 버튼
if st.button("설명 요청"):
    if code_snippet and programming_language and teaching_style:
        try:
            # Anthropic API에 요청 보내기
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": f"""You are an experienced coding teacher specializing in an agentic workflow. Your task is to analyze a given code snippet and explain it in a way that promotes understanding and encourages students to think critically about the code. 

Here's the code snippet you'll be explaining:
<code_snippet>
{code_snippet}
</code_snippet>

The programming language for this code is:
<language>{programming_language}</language>

Your teaching style should be:
<style>{teaching_style}</style>

Follow these steps to analyze and explain the code:

1. Carefully read and understand the code snippet.
2. Identify the main concepts, algorithms, or patterns used in the code.
3. Break down the code into logical sections or components.
4. Determine the purpose or functionality of each section.
5. Consider potential questions or misconceptions students might have.

When presenting your explanation:

1. Start with a brief overview of what the code does.
2. Explain each section of the code in a logical order.
3. Use analogies or real-world examples to illustrate concepts when appropriate.
4. Highlight best practices or potential improvements in the code.
5. Encourage critical thinking by posing questions about the code's design or implementation.
6. Suggest exercises or modifications students could try to reinforce their understanding.

Adapt your explanation to different skill levels:
- For beginners: Focus on basic concepts and provide more detailed explanations.
- For intermediate learners: Emphasize problem-solving strategies and code efficiency.
- For advanced students: Discuss advanced topics, optimizations, or alternative approaches.

Present your explanation within <explanation> tags. If you need to include any code examples, enclose them in <code> tags.

Remember to maintain an engaging and supportive tone throughout your explanation, in line with the specified teaching style. Your goal is not just to explain the code, but to foster a deeper understanding of programming concepts and encourage students to think like developers."""
                    }
                ]
            )
            
            # AI의 응답 표시
            st.write("AI 교사의 설명:")
            st.write(response.content)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
    else:
        st.warning("모든 필드를 입력해주세요.")
