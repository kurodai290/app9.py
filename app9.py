import streamlit as st

st.set_page_config(page_title="剣道昇段審査 練習アプリ", layout="wide")

st.title("🥋 剣道昇段審査 学科試験ドリル")
st.write("画像の問題をベースに作成しました。カッコに当てはまる言葉を選んでください。")

# スコア管理用
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- 問題2：心構え ---
with st.expander("問2. 剣道修錬の心構え", expanded=True):
    st.write("剣道を正しく学び、心身を修錬して旺盛なる（ ① ）を養い、剣道の特性を通じて（ ② ）を尊び、（ ③ ）を重んじ、（ ④ ）を尽くして常に自己の修養につとめ...")
    c1, c2, c3, c4 = st.columns(4)
    q2_1 = c1.selectbox("①", ["", "気力", "礼節", "信義", "誠意"], key="q21")
    q2_2 = c2.selectbox("②", ["", "気力", "礼節", "信義", "誠意"], key="q22")
    q2_3 = c3.selectbox("③", ["", "気力", "礼節", "信義", "誠意"], key="q23")
    q2_4 = c4.selectbox("④", ["", "気力", "礼節", "信義", "誠意"], key="q24")

# --- 問題3：中段の構え ---
with st.expander("問3. 中段の構え", expanded=True):
    st.write("中段の構えは、剣道の基本の構えであり、相手を（ ⑤ ）にも、自分を（ ⑥ ）にも、相手の（ ⑦ ）に応ずるにも都合のよい、いわゆる（ ⑧ ）の構えで...")
    c5, c6, c7, c8 = st.columns(4)
    q3_1 = c5.selectbox("⑤", ["", "攻める", "守る", "変化"], key="q31")
    q3_2 = c6.selectbox("⑥", ["", "攻める", "守る", "変化"], key="q32")
    q3_3 = c7.selectbox("⑦", ["", "攻める", "守る", "変化"], key="q33")
    q3_4 = c8.selectbox("⑧", ["", "正しい", "自在", "常態"], key="q34")

# --- 問題5：気剣体一致 ---
with st.expander("問5. 気剣体一致", expanded=True):
    st.write("気とは、心の（ ⑨ ）を言い、剣とは、剣の（ ⑩ ）を言い、体とは、身体の（ ⑪ ）をいう。")
    c9, c10, c11 = st.columns(3)
    q5_1 = c9.selectbox("⑨", ["", "活動状態", "運用状態", "行動状態"], key="q51")
    q5_2 = c10.selectbox("⑩", ["", "活動状態", "運用状態", "行動状態"], key="q52")
    q5_3 = c11.selectbox("⑪", ["", "活動状態", "運用状態", "行動状態"], key="q53")

# --- 問題6：一足一刀の間合 ---
with st.expander("問6. 一足一刀の間合", expanded=True):
    st.write("一足一刀の間合とは、一歩（ ⑫ ）相手に打突を与え、一歩（ ⑬ ）相手の打突をはずすことができる。")
    c12, c13 = st.columns(2)
    q6_1 = c12.selectbox("⑫", ["", "踏み込めば", "退けば"], key="q61")
    q6_2 = c13.selectbox("⑬", ["", "踏み込めば", "退けば"], key="q62")

# --- 判定ボタン ---
if st.button("採点する"):
    # 正解リスト
    results = [
        q2_1 == "気力", q2_2 == "礼節", q2_3 == "信義", q2_4 == "誠意",
        q3_1 == "攻める", q3_2 == "守る", q3_3 == "変化", q3_4 == "常態", # 画像の語群に基づくと「正しい」や「攻防自在」も候補ですがここでは一例
        q5_1 == "活動状態", q5_2 == "運用状態", q5_3 == "行動状態",
        q6_1 == "踏み込めば", q6_2 == "退けば"
    ]
    
    score = sum(results)
    st.write(f"### スコア: {score} / {len(results)}")
    
    if score == len(results):
        st.success("満点です！合格間違いなし！")
        st.balloons()
    else:
        st.warning("もう少しで見直し完了です。頑張りましょう！")
