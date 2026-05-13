import streamlit as st

# ページ設定
st.set_page_config(page_title="剣道昇段審査 完全版", layout="centered")

# --- 初期化 ---
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 全問題のデータ定義（正解データ）
QUESTIONS = [
    {"id": "q1", "title": "問1. 剣道の理念", "text": "剣道の理念を記入してください", "type": "text", "correct": "剣道は人間形成の道である"},
    {"id": "q2", "title": "問2. 修錬の心構え", "text": "旺盛なる（　）を養い...", "type": "select", "options": ["", "気力", "活力", "体力"], "correct": "気力"},
    {"id": "q3", "title": "問3. 中段の構え", "text": "中段は、いわゆる（　）の構えといわれ...", "type": "select", "options": ["", "常態", "基本", "攻防"], "correct": "常態"},
    {"id": "q4", "title": "問4. 切り返し", "text": "切り返しにより（　）が軽快闊達になる", "type": "select", "options": ["", "足さばき", "腕さばき", "体さばき"], "correct": "足さばき"},
    {"id": "q5", "title": "問5. 気剣体一致", "text": "「気」とは心の（　）をいう", "type": "select", "options": ["", "活動状態", "運用状態", "静止状態"], "correct": "活動状態"},
    {"id": "q6", "title": "問6. 一足一刀の間合", "text": "一歩（　）相手に打突を与えられる間合", "type": "select", "options": ["", "踏み込めば", "退けば", "止まれば"], "correct": "踏み込めば"},
    {"id": "q7", "title": "問7. 残心", "text": "相手を（　）した後でも油断しない心", "type": "select", "options": ["", "打突", "圧倒", "注視"], "correct": "打突"},
    {"id": "q8", "title": "問8. 有効打突", "text": "充実した気勢、（　）をもって...", "type": "select", "options": ["", "適正な姿勢", "強い打撃", "素早い動き"], "correct": "適正な姿勢"},
    {"id": "q9", "title": "問9. 竹刀の名称", "text": "竹刀の打突部を（　）という", "type": "select", "options": ["", "物打ち", "先革", "中結"], "correct": "物打ち"},
    {"id": "q10", "title": "問10. 稽古上の注意", "text": "道場内では常に（　）を守ること", "type": "select", "options": ["", "礼儀", "時間", "規則"], "correct": "礼儀"},
]

# --- ページ制御 ---
def next_page():
    st.session_state.page_index += 1

def reset_all():
    st.session_state.page_index = 0
    st.session_state.answers = {}

# --- メイン画面 ---
if st.session_state.page_index < len(QUESTIONS):
    # 問題回答フェーズ
    current_q = QUESTIONS[st.session_state.page_index]
    st.progress((st.session_state.page_index) / len(QUESTIONS))
    st.subheader(f"問題 {st.session_state.page_index + 1} / {len(QUESTIONS)}")
    st.header(current_q["title"])
    st.info(current_q["text"])

    if current_q["type"] == "text":
        user_ans = st.text_area("回答を入力", key=f"input_{current_q['id']}")
    else:
        user_ans = st.selectbox("選択肢から選ぶ", current_q["options"], key=f"input_{current_q['id']}")

    if st.button("次へ進む"):
        st.session_state.answers[current_q["id"]] = user_ans
        next_page()
        st.rerun()

else:
    # 最終結果フェーズ
    st.header("🏁 全ての問題が終了しました")
    st.write("あなたの回答と正解を照らし合わせます。")
    st.divider()

    score = 0
    for q in QUESTIONS:
        user_val = st.session_state.answers.get(q["id"], "")
        is_correct = False
        
        if q["type"] == "text":
            is_correct = q["correct"] in user_val
        else:
            is_correct = (user_val == q["correct"])
        
        if is_correct:
            score += 1
            st.success(f"**{q['title']}**\n\nあなたの回答: {user_val} （✅正解）")
        else:
            st.error(f"**{q['title']}**\n\nあなたの回答: {user_val if user_val else '未回答'}\n\n👉 正解: {q['correct']}")
    
    st.divider()
    st.subheader(f"合計得点: {score} / {len(QUESTIONS)}")
    
    if st.button("最初からやり直す"):
        reset_all()
        st.rerun()
