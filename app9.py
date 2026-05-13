import streamlit as st

# ページ設定
st.set_page_config(page_title="剣道昇段審査 全問網羅版", layout="wide")

# セッション状態の初期化
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def reset_answers():
    for key in st.session_state.keys():
        if key.startswith("ans_"):
            st.session_state[key] = ""
    st.session_state.submitted = False

# サイドバー：全10問を分割
st.sidebar.title("問題メニュー")
page = st.sidebar.radio("ページを選択", [
    "1. 理念と心構え (問1-2)",
    "2. 構えと切り返し (問3-4)",
    "3. 気剣体と間合 (問5-6)",
    "4. 残心と有効打突 (問7-8)",
    "5. 竹刀の名称とマナー (問9-10)"
])
if st.sidebar.button("全回答をリセット"):
    reset_answers()
    st.rerun()

st.title(f"🥋 {page}")

# 正誤判定用関数
def check_label(user_ans, correct_ans):
    if not st.session_state.submitted: return ""
    return "✅ 正解" if user_ans == correct_ans else f"❌ 不正解（正解: {correct_ans}）"

# --- 1. 問1-2 ---
if "1." in page:
    st.header("問1. 剣道の理念")
    ans_q1 = st.text_area("理念を記入してください", key="ans_q1", placeholder="剣道は...")
    if st.session_state.submitted:
        st.info("【正解】 剣道は人間形成の道である")

    st.header("問2. 修錬の心構え")
    q2_1 = st.selectbox("① 旺盛なる...", ["", "気力", "体力"], key="ans_q21")
    st.write(check_label(q2_1, "気力"))

# --- 2. 問3-4 ---
elif "2." in page:
    st.header("問3. 中段の構え")
    q3_1 = st.selectbox("⑧ 何の構え？", ["", "常態", "基本"], key="ans_q34")
    st.write(check_label(q3_1, "常態"))

    st.header("問4. 切り返しの効果")
    st.info("切り返しによって（ ⑭ ）が正しくなり、（ ⑮ ）が軽快闊達になり...")
    c1, c2 = st.columns(2)
    q4_1 = c1.selectbox("⑭ 何が正しくなる？", ["", "着装", "打突", "姿勢"], key="ans_q41")
    st.write(check_label(q4_1, "打突"))
    q4_2 = c2.selectbox("⑮ 何が軽快に？", ["", "足さばき", "体さばき", "腕さばき"], key="ans_q42")
    st.write(check_label(q4_2, "足さばき"))

# --- 3. 問5-6 ---
elif "3." in page:
    st.header("問5. 気剣体一致")
    q5_1 = st.selectbox("⑨ 気：心の...", ["", "活動状態", "運用状態"], key="ans_q51")
    st.write(check_label(q5_1, "活動状態"))

    st.header("問6. 一足一刀の間合")
    q6_1 = st.selectbox("⑫ 一歩（　）相手に打突を与える", ["", "踏み込めば", "退けば"], key="ans_q61")
    st.write(check_label(q6_1, "踏み込めば"))

# --- 4. 問7-8 ---
elif "4." in page:
    st.header("問7. 残心")
    q7_1 = st.selectbox("⑭ 相手を（　）した後...", ["", "打突", "圧倒"], key="ans_q71")
    st.write(check_label(q7_1, "打突"))

    st.header("問8. 有効打突")
    q8_1 = st.selectbox("⑮ 充実した気勢、（　）をもって...", ["", "適正な姿勢", "強い心"], key="ans_q81")
    st.write(check_label(q8_1, "適正な姿勢"))

# --- 5. 問9-10 ---
elif "5." in page:
    st.header("問9. 竹刀の名称")
    st.info("竹刀の打突部を（ ⑯ ）という。")
    q9_1 = st.selectbox("⑯ 名称を選択", ["", "物打ち", "先革", "鍔本"], key="ans_q91")
    st.write(check_label(q9_1, "物打ち"))

    st.header("問10. 稽古上の注意（マナー）")
    st.info("道場内では常に（ ⑰ ）を守り、相手に対して（ ⑱ ）を忘れないこと。")
    q10_1 = st.selectbox("⑰ 何を守る？", ["", "礼儀", "規則", "時間"], key="ans_q101")
    st.write(check_label(q10_1, "礼儀"))

# --- 共通ボタン ---
st.divider()
if st.button("採点・正解を表示"):
    st.session_state.submitted = True
    st.rerun()
