import streamlit as st
import random
import time
import base64
import json

# 1. ページ基本設定
st.set_page_config(page_title="Corporate Wars Premium", layout="wide")

st.markdown("""
<style>
    body { background-color: #121212; color: #e0e0e0; }
    h1 { color: #00ffcc !important; text-align: center; font-family: 'Helvetica Neue', Arial, sans-serif; }
    .stButton>button { width: 100%; border-radius: 4px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🏢 Corporate Wars Premium (Pure Python)")

# 2. セッションデータの初期化
if "company_id" not in st.session_state:
    st.session_state.company_id = ""
if "company_name" not in st.session_state:
    st.session_state.company_name = ""
if "ceo_name" not in st.session_state:
    st.session_state.ceo_name = ""
if "assets" not in st.session_state:
    st.session_state.assets = 2000
if "defense" not in st.session_state:
    st.session_state.defense = 100
if "staff" not in st.session_state:
    st.session_state.staff = {
        "intern": {"name": "インターン生", "cost": 500, "power": 5, "count": 0},
        "engineer": {"name": "シニアエンジニア", "cost": 3000, "power": 40, "count": 0},
        "sales": {"name": "敏腕営業マン", "cost": 15000, "power": 250, "count": 0},
        "ai": {"name": "生成AI自動エージェント", "cost": 80000, "power": 1800, "count": 0}
    }
if "products" not in st.session_state:
    st.session_state.products = {
        "app": {"name": "暇つぶしSNSアプリ開発", "cost": 5000, "multi": 1.2, "done": False},
        "ec": {"name": "次世代ECモール構築", "cost": 35000, "multi": 1.5, "done": False},
        "ev": {"name": "自動運転空飛ぶクルマ開発", "cost": 250000, "multi": 2.5, "done": False}
    }
if "competitors" not in st.session_state:
    st.session_state.competitors = {}
if "last_tick" not in st.session_state:
    st.session_state.last_tick = time.time()

# 3. 自動売上回収の計算
current_time = time.time()
elapsed = int(current_time - st.session_state.last_tick)

if elapsed > 0 and st.session_state.company_name:
    base_power = sum(s["count"] * s["power"] for s in st.session_state.staff.values())
    multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            multiplier *= p["multi"]
    st.session_state.assets += int(base_power * multiplier) * elapsed
    st.session_state.last_tick = current_time

# --- 4. 未ログイン画面（会社設立） ---
if not st.session_state.company_name:
    st.subheader("新規企業の創立登記申請")
    st.info("好きな会社名とあなたの名前を入力して、ゲームを開始してください。")
    
    input_corp = st.text_input("新しい会社名", key="init_corp", placeholder="サイバーコア株式会社")
    input_ceo = st.text_input("代表取締役CEO（あなたの名前）", key="init_ceo", placeholder="あなたの名前")
    
    if st.button("会社を設立して市場に参入する", type="primary"):
        if input_corp.strip() and input_ceo.strip():
            st.session_state.company_id = f"corp_{random.randint(100000, 999999)}"
            st.session_state.company_name = input_corp.strip()
            st.session_state.ceo_name = input_ceo.strip()
            st.session_state.last_tick = time.time()
            st.rerun()
        else:
            st.error("すべての項目を入力してください。")
            
    st.markdown("---")
    with st.expander("🤝 既存のマルチプレイ市場に参加する（同期コードをお持ちの方）"):
        sync_code = st.text_input("同期用データコードを貼り付けてください")
        if st.button("データを同期して合流"):
            if sync_code.strip():
                try:
                    decoded = json.loads(base64.b64decode(sync_code.strip()).decode('utf-8'))
                    st.session_state.competitors.update(decoded)
                    st.success("市場データを読み込みました！会社設立後に「世界の市場記録」を確認してください。")
                except Exception:
                    st.error("同期コードの解析に失敗しました。")

# --- 5. メインゲーム画面 ---
else:
    # リアルタイムの生産力と株価の計算
    base_power = sum(s["count"] * s["power"] for s in st.session_state.staff.values())
    multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            multiplier *= p["multi"]
    auto_power = int(base_power * multiplier)
    
    stock_base = (st.session_state.assets * 0.05) + (sum(s["count"] for s in st.session_state.staff.values()) * 50) + (sum(1 for p in st.session_state.products.values() if p["done"]) * 1000)
    stock_price = max(10, int(stock_base * random.uniform(0.97, 1.03)))
    
    # 画面上部ステータス
    col1, col2, col3 = st.columns(3)
    col1.metric(label="自社総資産", value=f"￥{st.session_state.assets:,}")
    col2.metric(label="自社現在株価", value=f"￥{stock_price:,}")
    col3.metric(label="社員数 / 生産力", value=f"{sum(s['count'] for s in st.session_state.staff.values())} 名 / {auto_power:,}秒")
    
    # タブメニュー
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏢 自社概念", "👥 社員雇用", "🧪 新商品開発", "📈 株価専用窓口", "⚔️ 世界の市場記録"])
    
    # TAB 1: 自社概念
    with tab1:
        st.subheader("企業アイデンティティ")
        st.write(f"**会社名:** {st.session_state.company_name}")
        st.write(f"**最高経営責任者 (CEO):** {st.session_state.ceo_name}")
        st.write(f"**セキュリティ防衛力:** {st.session_state.defense} DEF")
        
        st.markdown("### 経営アクション")
        c1, c2, c3 = st.columns(3)
        if c1.button("社長自ら営業活動を行う (+￥100)"):
            st.session_state.assets += 100
            st.rerun()
        if c2.button("セキュリティを強化 (-￥1,000 / +100 DEF)"):
            if st.session_state.assets >= 1000:
                st.session_state.assets -= 1000
                st.session_state.defense += 100
                st.rerun()
            else:
                st.error("資金が不足しています。")
        if c3.button("画面をリロード（時間を進めて売上回収）"):
            st.rerun()
            
        st.markdown("---")
        st.subheader("🤝 マルチプレイ同期（コード共有）")
        my_data = {
            st.session_state.company_id: {
                "name": st.session_state.company_name,
                "ceo": st.session_state.ceo_name,
                "assets": st.session_state.assets,
                "defense": st.session_state.defense,
                "stockPrice": stock_price
            }
        }
        my_data.update(st.session_state.competitors)
        encoded_data = base64.b64encode(json.dumps(my_data).encode('utf-8')).decode('utf-8')
        st.text_area("あなたのデータコード（ライバルに送ってください）", value=encoded_data, height=100)
        
        active_sync = st.text_input("追加するライバルのコードを貼り付け", key="active_sync")
        if st.button("追加同期を実行"):
            if active_sync.strip():
                try:
                    decoded = json.loads(base64.b64decode(active_sync.strip()).decode('utf-8'))
                    st.session_state.competitors.update(decoded)
                    st.success("ライバルデータを追加しました！")
                    st.rerun()
                except Exception:
                    st.error("同期失敗")

    # TAB 2: 社員雇用
    with tab2:
        st.subheader("人材マネジメント")
        for s_id, staff in st.session_state.staff.items():
            box = st.container(border=True)
            box.markdown(f"**{staff['name']}** (現在: {staff['count']}名) — コスト: ￥{staff['cost']:,} / 労働力: +{staff['power']}/秒")
            if box.button(f"{staff['name']}を雇用", key=f"btn_buy_{s_id}"):
                if st.session_state.assets >= staff["cost"]:
                    st.session_state.assets -= staff["cost"]
                    st.session_state.staff[s_id]["count"] += 1
                    st.session_state.staff[s_id]["cost"] = int(staff["cost"] * 1.15)
                    st.rerun()
                else:
                    st.error("資金不足")

    # TAB 3: 新商品開発
    with tab3:
        st.subheader("プロダクト開発")
        for p_id, prod in st.session_state.products.items():
            box = st.container(border=True)
            status = "【開発完了】" if prod["done"] else f"費用: ￥{prod['cost']:,}"
            box.markdown(f"**{prod['name']}** ({status}) — ボーナス: 全体売上 {prod['multi']} 倍")
            if not prod["done"]:
                if box.button(f"{prod['name']}へ投資", key=f"btn_prod_{p_id}"):
                    if st.session_state.assets >= prod["cost"]:
                        st.session_state.assets -= prod["cost"]
                        st.session_state.products[p_id]["done"] = True
                        st.rerun()
                    else:
                        st.error("資金不足")

    # TAB 4: 株価窓口
    with tab4:
        st.subheader("証券取引情報")
        market_cap = stock_price * 10000
        rank = "E"
        if stock_price > 5000: rank = "S"
        elif stock_price > 2000: rank = "A"
        elif stock_price > 1000: rank = "B"
        elif stock_price > 500: rank = "C"
        elif stock_price > 200: rank = "D"
        
        sc1, sc2 = st.columns(2)
        sc1.metric(label="仮想時価総額評価", value=f"￥{market_cap:,}")
        sc2.metric(label="企業格付ランク", value=rank)

    # TAB 5: 世界の市場記録
    with tab5:
        st.subheader("競合他社一覧")
        display_count = 0
        for comp_id, comp in list(st.session_state.competitors.items()):
            if comp_id == st.session_state.company_id:
                continue
            display_count += 1
            
            box = st.container(border=True)
            box.markdown(f"🔴 **{comp['name']}** (CEO: {comp['ceo']}) | 資産: ￥{comp['assets']:,} | 株価: ￥{comp['stockPrice']:,} | 防衛力: {comp['defense']} DEF")
            if box.button(f"{comp['name']}へ買収作戦を実行 (コスト￥1,500)", key=f"btn_atk_{comp_id}"):
                if st.session_state.assets >= 1500:
                    st.session_state.assets -= 1500
                    damage = random.randint(20, 70) + (sum(s['count'] for s in st.session_state.staff.values()) * 2)
                    st.session_state.competitors[comp_id]["defense"] -= damage
                    
                    if st.session_state.competitors[comp_id]["defense"] <= 0:
                        st.balloons()
                        st.success(f"🎉 {comp['name']} の買収に成功しました！資産 ￥{comp['assets']:,} を吸収します。")
                        st.session_state.assets += comp['assets']
                        del st.session_state.competitors[comp_id]
                    else:
                        st.warning(f"⚔️ 敵企業の防衛力を {damage} 削りました！")
                    st.rerun()
                else:
