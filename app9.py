import streamlit as st

st.set_page_config(page_title="剣道昇段審査 穴埋めドリル", layout="centered")

st.title("🥋 剣道昇段審査 穴埋め練習")
st.write("画像の問題を再現しました。適切な言葉を選んでください。")

# --- 問題2 ---
st.header("問2. 剣道修錬の心構え")
st.info("剣道を正しく学び、心身を修錬して旺盛なる ( ① ) を養い、剣道の特性を通じて ( ② ) を尊び、( ③ ) を重んじ、( ④ ) を尽くして常に自己の修養につとめ...")

col1, col2 = st.columns(2)
with col1:
    ans1 = st.selectbox("①の答え", ["---", "気力", "礼節", "信義", "誠意"])
    ans2 = st.selectbox("②の答え", ["---", "気力", "礼節", "信義", "誠意"])
with col2:
    ans3 = st.selectbox("③の答え", ["---", "気力", "礼節", "信義", "誠意"])
    ans4 = st.selectbox("④の答え", ["---", "気力", "礼節", "信義", "誠意"])

# --- 問題6 ---
st.header("問6. 一足一刀の間合")
st.info("一足一刀の間合とは、一歩 ( ⑤ ) 相手に打突を与え、一歩 ( ⑥ ) 相手の打突をはずすことができる。")

col3, col4 = st.columns(2)
with col3:
    ans5 = st.selectbox("⑤の答え", ["---", "踏み込めば", "退けば", "攻めれば"])
with col4:
    ans6 = st.selectbox("⑥の答え", ["---", "踏み込めば", "退けば", "攻めれば"])

# --- 答え合わせ ---
if st.button("答え合わせをする"):
    correct_count = 0
    if ans1 == "気力": correct_count += 1
    if ans2 == "礼節": correct_count += 1
    if ans3 == "信義": correct_count += 1
    if ans4 == "誠意": correct_count += 1
    if ans5 == "踏み込めば": correct_count += 1
    if ans6 == "退けば": correct_count += 1
    
    st.success(f"結果: 6問中 {correct_count} 門正解です！")
    if correct_count == 6:
        st.balloons()
