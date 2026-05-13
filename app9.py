import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="剣道初段 学科ドリル（記述対応版）", layout="centered")

# --- 初段：データベース（記述問題を強化） ---
if "shodan_db" not in st.session_state:
    st.session_state.shodan_db = [
        {"id": 1, "title": "問1. 剣道の理念", "text": "全日本剣道連盟制定の「剣道の理念」を記せ。", "type": "text", "correct": "剣道は人間形成の道である", "keyword": "人間形成"},
        {"id": 2, "title": "問2. 心構え", "text": "旺盛なる（　）を養い...", "type": "select", "options": ["", "気力", "活力", "体力"], "correct": "気力"},
        {"id": 3, "title": "問2. 心構え", "text": "剣道の特性を通じて何を尊び、何を重んじるか？（記述）", "type": "text", "correct": "礼節を尊び、信義を重んじ", "keyword": "礼節"},
        {"id": 4, "title": "問2. 心構え", "text": "国家社会を愛して広く人類の（　）に寄与せんとする。", "type": "select", "options": ["", "平和繁栄", "相互理解"], "correct": "平和繁栄"},
        {"id": 5, "title": "問3. 中段の構え", "text": "中段の構えは、いわゆる何の構えといわれるか？（記述）", "type": "text", "correct": "攻防自在の構え", "keyword": "攻防自在"},
        {"id": 6, "title": "問3. 中段の構え", "text": "中段は、もっとも（　）な構えである。", "type": "select", "options": ["", "正しい", "自然", "強力"], "correct": "正しい"},
        {"id": 7, "title": "問4. 切り返しの意義", "text": "切り返しは何の動きを巧妙にするか？（記述）", "type": "text", "correct": "手の内の動き", "keyword": "手の内"},
        {"id": 8, "title": "問4. 切り返しの意義", "text": "進退の動作を早くし、（　）を正確に知ることができる。", "type": "select", "options": ["", "間合", "機会", "打突"], "correct": "間合"},
        {"id": 9, "title": "問4. 切り返しの意義", "text": "何の技を修練するものか？（記述）", "type": "text", "correct": "気剣体の一致の技", "keyword": "気剣体"},
        {"id": 10, "title": "問5. 気剣体一致", "text": "「気」とは何の（　）をいうか？", "type": "select", "options": ["", "活動状態", "運用状態", "行動状態"], "correct": "活動状態"},
        {"id": 11, "title": "問5. 気剣体一致", "text": "「剣」とは剣の（　）、「体」とは身体の（　）をいう。", "type": "select", "options": ["", "運用状態・行動状態", "行動状態・運用状態"], "correct": "運用状態・行動状態"},
        {"id": 12, "title": "問6. 一足一刀の間合", "text": "一歩（　）相手に打突を与え、一歩（　）相手の打突をはずす。", "type": "select", "options": ["", "攻めれば・退けば", "踏み込めば・引けば"], "correct": "攻めれば・退けば"},
        {"id": 13, "title": "問6. 一足一刀の間合", "text": "いわゆる（　）に強く、守りにも強い間合。", "type": "select", "options": ["", "攻め", "技", "心"], "correct": "攻め"},
        {"id": 14, "title": "問7. 残心", "text": "残心とは、相手を（　）した後でも心を緩めないこと。", "type": "select", "options": ["", "打突", "圧倒", "制覇"], "correct": "打突"},
        {"id": 15, "title": "問7. 残心", "text": "残心とは、どのような用意のことか？（記述）", "type": "text", "correct": "身構え、心構えを示し、相手の反撃を制する", "keyword": "反撃"},
        {"id": 16, "title": "問8. 有効打突", "text": "有効打突の要素を2つ記せ。（記述）", "type": "text", "correct": "充実した気勢、適正な姿勢", "keyword": "充実"},
        {"id": 17, "title": "問8. 有効打突", "text": "竹刀のどこで、どのように打突すべきか？（記述）", "type": "text", "correct": "打突部（物打ち）で刃筋正しく打突する", "keyword": "刃筋"},
        {"id": 18, "title": "問9. 日本剣道形の重要性", "text": "剣道形は何の基本を示すものか？（記述）", "type": "text", "correct": "剣技のもっとも大事な基本", "keyword": "基本"},
        {"id": 19, "title": "問9. 日本剣道形の重要性", "text": "剣道形は何の「理合」といえるか？（記述）", "type": "text", "correct": "術技の理合", "keyword": "理合"},
        {"id": 20, "title": "問10. 日本剣道形の一本目", "text": "打太刀・仕太刀ともにどのような構えか？", "type": "select", "options": ["", "左上段", "右上段", "中段"], "correct": "左上段"},
        {"id": 21, "title": "問10. 日本剣道形の一本目", "text": "打太刀は仕太刀のどこを打つか？", "type": "select", "options": ["", "面", "小手", "胴"], "correct": "面"},
        {"id": 22, "title": "問10. 日本剣道形の一本目", "text": "打ち下ろした剣先はどこの高さになるか？（記述）", "type": "text", "correct": "膝頭よりもやや低くなる", "keyword": "膝頭"},
        {"id": 23, "title": "共通：竹刀", "text": "竹刀の「中結い」から「先革」までを何という？（記述）", "type": "text", "correct": "物打ち", "keyword": "物打ち"},
        {"id": 24, "title": "共通：礼儀", "text": "稽古の前後に行う相互の礼は何を忘れないためか？（記述）", "type": "text", "correct": "相手を尊重する心", "keyword": "尊重"},
        {"id": 25, "title": "問4. 切り返し", "text": "切り返しは（　）を養うためのものである。", "type": "select", "options": ["", "体力気力", "勝負勘", "スピード"], "correct": "体力気力"},
        {"id": 26, "title": "問7. 残心", "text": "相手に（　）を示し、（　）を示す。", "type": "select", "options": ["", "身構え・心構え", "威圧・動作"], "correct": "身構え・心構え"},
        {"id": 27, "title": "問8. 有効打突", "text": "打突後には何があるものとするか？", "type": "select", "options": ["", "残心", "気合", "審判の宣告"], "correct": "残心"},
        {"id": 28, "title": "共通：理念", "text": "「人間形成」とは、心を鍛え、何を磨くことか？（記述）", "type": "text", "correct": "人格を磨く", "keyword": "人格"},
        {"id": 29, "title": "共通：構え", "text": "構えを解くとき、剣先はどこに向けるか？", "type": "select", "options": ["", "右下", "左下", "正面"], "correct": "右下"},
        {"id": 30, "title": "共通：審査", "text": "審査において、最も重要視される構えは？", "type": "select", "options": ["", "中段の構え", "上段の構え", "下段の構え"], "correct": "中段の構え"},
    ]

# --- セッション管理 ---
if "test_set" not in st.session_state:
    st.session_state.test_set = random.sample(st.session_state.shodan_db, 10)
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "user_ans" not in st.session_state:
    st.session_state.user_ans = {}
if "done" not in st.session_state:
    st.session_state.done = False

def restart():
    st.session_state.test_set = random.sample(st.session_state.shodan_db, 10)
    st.session_state.current_idx = 0
    st.session_state.user_ans = {}
    st.session_state.done = False
    st.rerun()

# --- メイン ---
st.title("🥋 初段学科ドリル（記述・選択）")

if not st.session_state.done:
    q = st.session_state.test_set[st.session_state.current_idx]
    
    st.progress(st.session_state.current_idx / 10)
    st.subheader(f"問題 {st.session_state.current_idx + 1} / 10")
    st.markdown(f"### {q['title']}")
    st.info(q['text'])
    
    if q["type"] == "text":
        ans = st.text_area("回答を入力してください", key=f"t_{q['id']}")
    else:
        ans = st.radio("選択してください", q['options'], key=f"r_{q['id']}")
    
    c1, c2 = st.columns(2)
    if st.session_state.current_idx < 9:
        if c1.button("次へ進む"):
            st.session_state.user_ans[q['id']] = ans
            st.session_state.current_idx += 1
            st.rerun()
    else:
        if c1.button("採点する"):
            st.session_state.user_ans[q['id']] = ans
            st.session_state.done = True
            st.rerun()
    
    if c2.button("途中で採点"):
        st.session_state.done = True
        st.rerun()

else:
    st.header("🏁 採点結果")
    score = 0
    for q in st.session_state.test_set:
        val = st.session_state.user_ans.get(q['id'], "未回答")
        # 記述式はキーワードが含まれているかチェック
        is_ok = q.get("keyword", "NONE") in val if q["type"] == "text" else (val == q["correct"])
        if is_ok: score += 1
        
        with st.expander(f"{q['title']}：{'✅' if is_ok else '❌'}"):
            st.write(f"問題: {q['text']}")
            st.write(f"あなたの回答: {val}")
            st.write(f"模範解答: {q['correct']}")

    st.subheader(f"スコア: {score} / 10")
    if score >= 8: st.balloons()
    if st.button("もう一度挑戦"): restart()
