import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="剣道昇段審査 対策", layout="centered")

# --- 問題データ ---
ALL_QUESTIONS = [
    {"id": "q1", "title": "問1. 剣道の理念", "text": "剣道の理念を記入してください", "type": "text", "correct": "人間形成の道"},
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

# --- セッション初期化 ---
if "questions_list" not in st.session_state:
    st.session_state.questions_list = random.sample(ALL_QUESTIONS, len(ALL_QUESTIONS))
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "finished" not in st.session_state:
    st.session_state.finished = False

# --- 関数 ---
def reset_game():
    st.session_state.questions_list = random.sample(ALL_QUESTIONS, len(ALL_QUESTIONS))
    st.session_state.page_index = 0
    st.session_state.answers = {}
    st.session_state.finished = False
    st.rerun()

def finish_game():
    st.session_state.finished = True
    st.rerun()

# --- サイドバー ---
st.sidebar.title("操作パネル")
if not st.session_state.finished:
    st.sidebar.warning("まだ途中の場合でも、下のボタンで現在の状況を採点できます。")
    if st.sidebar.button("途中でやめて採点する"):
        finish_game()
st.sidebar.divider()
if st.sidebar.button("最初からやり直す"):
    reset_game()

# --- メイン画面 ---
if not st.session_state.finished and st.session_state.page_index < len(st.session_state.questions_list):
    # 【回答フェーズ】
    current_q = st.session_state.questions_list[st.session_state.page_index]
    
    st.progress(st.session_state.page_index / len(st.session_state.questions_list))
    st.subheader(f"問題 {st.session_state.page_index + 1} / {len(st.session_state.questions_list)}")
    st.header(current_q["title"])
    st.info(current_q["text"])

    if current_q["type"] == "text":
        user_ans = st.text_area("回答を入力", key=f"input_{current_q['id']}")
    else:
        user_ans = st.selectbox("選択肢から選ぶ", current_q["options"], key=f"input_{current_q['id']}")

    if st.button("次へ進む"):
        st.session_state.answers[current_q["id"]] = user_ans
        st.session_state.page_index += 1
        st.rerun()
else:
    # 【結果表示フェーズ】
    st.header("🏁 採点結果")
    score = 0
    answered_count = len(st.session_state.answers)
    
    # 回答した問題だけ、あるいは全問表示
    for q in st.session_state.questions_list:
        user_val = st.session_state.answers.get(q["id"], "")
        if user_val == "" and not st.session_state.finished: continue # 未回答は飛ばす（通常終了時用）
        
        is_correct = q["correct"] in user_val if q["type"] == "text" else (user_val == q["correct"])
        
        with st.expander(f"{q['title']} - {'✅正解' if is_correct else '❌不正解'}"):
            st.write(f"**あなたの回答:** {user_val if user_val else '(未回答)'}")
            st.write(f"**正しい答え:** {q['correct']}")
            if is_correct: score += 1

    st.divider()
    st.subheader(f"正解数: {score} / {len(st.session_state.questions_list)}")
    if score >= 8:
        st.balloons()
        st.success("素晴らしい！合格圏内です。")
    
    if st.button("もう一度最初から挑戦する"):
        reset_game()
