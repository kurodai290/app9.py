import streamlit as st

# ページ設定
st.set_page_config(page_title="剣道昇段審査 練習アプリ", layout="wide")

# セッション状態の初期化（リセット機能用）
def reset_answers():
    for key in st.session_state.keys():
        if key.startswith("ans_"):
            st.session_state[key] = ""
    st.session_state.submitted = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# サイドバーでページ選択
st.sidebar.title("メニュー")
page = st.sidebar.radio("問題を選択", ["問2-3: 心構えと中段", "問5-6: 気剣体と間合", "問7-8: 残心と有効打突"])
if st.sidebar.button("全回答をリセット"):
    reset_answers()

st.title(f"🥋 剣道昇段審査：{page}")

# 正誤判定用の関数
def check_label(user_ans, correct_ans):
    if not st.session_state.submitted:
        return ""
    return "✅ 正解" if user_ans == correct_ans else f"❌ 不正解（正解: {correct_ans}）"

# --- ページ1：問2と問3 ---
if page == "問2-3: 心構えと中段":
    st.header("問2. 剣道修錬の心構え")
    st.info("剣道を正しく学び、心身を修錬して旺盛なる（ ① ）を養い、剣道の特性を通じて（ ② ）を尊び、（ ③ ）を重んじ、（ ④ ）を尽くして常に自己の修養につとめ...")
    
    col1, col2 = st.columns(2)
    ans2_1 = col1.selectbox("①の答え", ["", "気力", "礼節", "信義", "誠意"], key="ans_q21")
    st.write(check_label(ans2_1, "気力"))
    
    ans2_2 = col2.selectbox("②の答え", ["", "気力", "礼節", "信義", "誠意"], key="ans_q22")
    st.write(check_label(ans2_2, "礼節"))

    st.header("問3. 中段の構え")
    st.info("中段の構えは、相手を（ ⑤ ）にも、自分を（ ⑥ ）にも適した...")
    ans3_1 = st.selectbox("⑤ 相手を...", ["", "攻める", "守る", "変化"], key="ans_q31")
    st.write(check_label(ans3_1, "攻める"))

# --- ページ2：問5と問6 ---
elif page == "問5-6: 気剣体と間合":
    st.header("問5. 気剣体一致")
    st.info("気とは心の（ ⑨ ）、剣とは剣の（ ⑩ ）、体とは身体の（ ⑪ ）をいう。")
    
    ans5_1 = st.selectbox("⑨ 気：心の...", ["", "活動状態", "運用状態", "行動状態"], key="ans_q51")
    st.write(check_label(ans5_1, "活動状態"))
    
    ans5_2 = st.selectbox("⑩ 剣：剣の...", ["", "活動状態", "運用状態", "行動状態"], key="ans_q52")
    st.write(check_label(ans5_2, "運用状態"))

    st.header("問6. 一足一刀の間合")
    ans6_1 = st.selectbox("⑫ 一歩（　）相手に打突を与える", ["", "踏み込めば", "退けば"], key="ans_q61")
    st.write(check_label(ans6_1, "踏み込めば"))

# --- ページ3：問7と問8 ---
elif page == "問7-8: 残心と有効打突":
    st.header("問7. 残心について")
    st.info("残心とは、相手を（ ⑭ ）した後でも油断せず...")
    ans7_1 = st.selectbox("⑭ 相手を...", ["", "打突", "制圧", "威圧"], key="ans_q71")
    st.write(check_label(ans7_1, "打突"))

    st.header("問8. 有効打突")
    st.info("有効打突とは、充実した気勢、（ ⑮ ）をもって...")
    ans8_1 = st.selectbox("⑮ 何をもって？", ["", "適正な姿勢", "残心", "刃筋正しく"], key="ans_q81")
    st.write(check_label(ans8_1, "適正な姿勢"))

# --- 共通の採点ボタン ---
st.divider()
if st.button("このページの採点をする"):
    st.session_state.submitted = True
    st.rerun()
