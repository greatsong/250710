import streamlit as st

st.set_page_config(page_title="MBTI 여행지 추천", page_icon="🌍")

st.title("✈️ MBTI 유형별 여행지 추천")
st.markdown("당신의 성격에 딱 맞는 여행지를 추천해드릴게요! 🧳")

mbti_list = [
    "ENFP", "INFP", "ENFJ", "INFJ",
    "ENTP", "INTP", "ENTJ", "INTJ",
    "ESFP", "ISFP", "ESFJ", "ISFJ",
    "ESTP", "ISTP", "ESTJ", "ISTJ"
]

mbti = st.selectbox("👉 당신의 MBTI를 선택해주세요:", mbti_list)

if mbti:
    st.balloons()

    recommendations = {
        "ENFP": [
            ("바르셀로나 🇪🇸", "가우디 건축물 투어 🏰", "창의적이고 자유로운 ENFP에게 예술 감성과 열정이 넘치는 도시예요."),
            ("치앙마이 🇹🇭", "나이트 마켓 & 코끼리 보호구역 🐘", "다정한 ENFP에게 동물과 교감할 수 있는 경험은 최고의 힐링!"),
            ("부에노스아이레스 🇦🇷", "탱고 공연 관람 💃", "열정적인 분위기에서 새로운 문화를 마음껏 즐겨보세요!")
        ],
        "INTJ": [
            ("도쿄 🇯🇵", "미래형 박물관 & 아키하바라 탐방 🤖", "논리적이고 혁신을 좋아하는 INTJ에게 최고의 도시."),
            ("레퀴야비크 🇮🇸", "오로라 관측 & 고요한 대자연 감상 🌌", "혼자만의 시간을 가치 있게 보내고 싶다면 추천!"),
            ("베를린 🇩🇪", "역사 박물관 투어 & 창의적 예술 공간 🎨", "깊은 사고와 통찰을 자극하는 여행지예요.")
        ],
        "ISFP": [
            ("호이안 🇻🇳", "랜턴 거리 산책 & 강변 카페 ☕", "감성적인 ISFP에게 조용하고 예쁜 거리 풍경은 최고의 힐링."),
            ("울릉도 🇰🇷", "섬 트레킹 & 독도 전망대 🏝️", "자연과의 조용한 교감이 잘 맞는 성향이에요."),
            ("코펜하겐 🇩🇰", "니하운 산책 & 자전거 투어 🚲", "자유로운 감성과 심플함을 동시에 느낄 수 있어요.")
        ],
        # 생략된 유형은 아래와 같이 추가하면 됩니다.
        "ENTP": [
            ("뉴욕 🇺🇸", "브로드웨이 공연 & 박물관 투어 🎭", "아이디어와 자극을 좋아하는 ENTP에게 완벽한 도시예요."),
            ("홍콩 🇭🇰", "피크트램 타고 도시야경 감상 🌃", "빠르게 변화하는 도시를 즐기며 새로운 경험을 쌓을 수 있어요."),
            ("리스본 🇵🇹", "트램 여행 & 거리 예술 탐방 🚌", "모험심 강한 ENTP에게 매일이 흥미로운 장소입니다.")
        ]
        # 나머지 MBTI도 같은 방식으로 추가 가능
    }

    if mbti in recommendations:
        st.subheader(f"📌 {mbti} 유형에게 추천하는 여행지 TOP 3")
        for city, place, reason in recommendations[mbti]:
            st.markdown(f"### {city}")
            st.markdown(f"- **추천 명소:** {place}")
            st.markdown(f"- **추천 이유:** {reason}")
            st.markdown("---")
    else:
        st.info("아직 이 MBTI에 대한 여행 정보는 준비 중이에요. 곧 추가될 예정입니다! ✍️")
