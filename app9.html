import streamlit as st
import random
import time
import base64
import json

# 1. ページ設定とスタイル適用
st.set_page_config(page_title="Corporate Wars Premium", layout="wide")

st.markdown("""
<style>
    body { background-color: #121212; color: #e0e0e0; }
    h1 { color: #00ffcc !important; text-align: center; }
    .stButton>button { width: 100%; border-radius: 4px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🏢 Corporate Wars Premium (Pure Python Edition)")

# 2. セッション状態（ゲームデータ）の初期化
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

# 3. バックグラウンド時間経過処理
current_time = time.time()
elapsed_seconds = int(current_time - st.session_state.last_tick)

if elapsed_seconds > 0 and st.session_state.company_name:
    base_power = sum(s["count"] * s["power"] for s in st.session_state.staff.values())
    multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            multiplier *= p["multi"]
    auto_power = int(base_power * multiplier)
    st.session_state.assets += auto_power * elapsed_seconds
    st.session_state.last_tick = current_time

# --- 画面描画ロジック ---

# 【未ログイン状態】
if not st.session_state.company_name:
    st.subheader("新規企業の創立登記申請")
    st.info("初めてプレイする方は、ここから自分の会社を設立してスタートしてください。")
    
    input_corp = st.text_input("新しい会社名（例：サイバーコア株式会社）", key="init_corp")
    input_ceo = st.text_input("代表取締役CEO（あなたの名前）", key="init_ceo")
    
    if st.button("会社を設立して市場に参入する", type="primary"):
        if input_corp.strip() and input_ceo.strip():
            st.session_state.company_id = f"corp_{random.randint(100000, 999999)}"
            st.session_state.company_name = input_corp.strip()
            st.session_state.ceo_name = input_ceo.strip()
            st.session_state.last_tick = time.time()
            st.rerun()
        else:
            st.error("会社名とCEO名を入力してください。")
            
    st.markdown("---")
    with st.expander("🤝 既存のマルチプレイ市場に参加する（同期コードをお持ちの方）"):
        sync_code = st.text_input("ライバルから貰った「同期用データコード」を貼り付けてください")
        if st.button("データを同期して合流"):
            if sync_code.strip():
                try:
                    decoded = json.loads(base64.b64decode(sync_code.strip()).decode('utf-8'))
                    st.session_state.competitors.update(decoded)
                    st.success("ライバルの市場データを同期しました！会社設立後に「世界の市場記録」を確認してください。")
                except Exception:
                    st.error("データの同期に失敗しました。コードが正しいか確認してください。")

# 【ログイン状態：メインゲーム画面】
else:
    base_power = sum(s["count"] * s["power"] for s in st.session_state.staff.values())
    multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            multiplier *= p["multi"]
    auto_power = int(base_power * multiplier)
    
    stock_base = (st.session_state.assets * 0.05) + (sum(s["count"] for s in st.session_state.staff.values()) * 50) + (sum(1 for p in st.session_state.products.values() if p["done"]) * 1000)
    stock_price = max(10, int(stock_base * random.uniform(0.97, 1.03)))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="自社総資産", value=f"￥{st.session_state.assets:,}")
    with col2:
        st.metric(label="自社現在株価", value=f"￥{stock_price:,}")
    with col3:
        st.metric(label="社員数 / 生産力", value=f"{sum(s['count'] for s in st.session_state.staff.values())} 名 / {auto_power:,}秒")
        
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏢 自社概念", "👥 社員雇用", "🧪 新商品開発", "📈 株価専用窓口", "⚔️ 世界の市場記録"])
    
    # PAGE 1: 自社概念
    with tab1:
        st.subheader("企業アイデンティティ")
        st.write(f"**会社名:** {st.session_state.company_name}")
        st.write(f"**最高経営責任者 (CEO):** {st.session_state.ceo_name}")
        st.write(f"**セキュリティ防衛力:** {st.session_state.defense} DEF")
        
        st.markdown("### 経営アクション")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("社長自ら営業活動を行う (+￥100)"):
                st.session_state.assets += 100
                st.rerun()
        with c2:
            if st.button("セキュリティを強化 (-￥1,000 / +100 DEF)"):
                if st.session_state.assets >= 1000:
                    st.session_state.assets -= 1000
                    st.session_state.defense += 100
                    st.rerun()
                else:
                    st.error("資金が不足しています。")
        with c3:
            if st.button("画面をリロード（時間を進めて売上回収）"):
                st.rerun()
                
        st.markdown("---")
        st.subheader("🤝 マルチプレイ同期（ライバルを招待）")
        st.write("下のボックスの暗号コードをコピーしてライバルに渡してください。")
        
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
        
        st.text_area("あなたの市場データコード（コピーして共有してください）", value=encoded_data, height=100)
        
        st.markdown("### ライバルのコードを追加インポートする")
        active_sync_code = st.text_input("追加するライバルのコードを貼り付け", key="active_sync")
        if st.button("追加同期を実行"):
            if active_sync_code.strip():
                try:
                    decoded = json.loads(base64.b64decode(active_sync_code.strip()).decode('utf-8'))
                    st.session_state.competitors.update(decoded)
                    st.success("ライバルデータをインポートしました！")
                    st.rerun()
                except Exception:
                    st.error("同期に失敗しました。")

    # PAGE 2: 社員雇用
    with tab2:
        st.subheader("人材マネジメント")
        for s_id, staff in st.session_state.staff.items():
            col_info, col_btn = st.columns([3, 1])
            with col_info:
                st.markdown(f"**{staff['name']}** (現在: {staff['count']}名)<br><span style='color:#aaa;'>雇用コスト: ￥{staff['cost']:,} | 労働力: +{staff['power']}/秒</span>", unsafe_allow_html=True)
            with col_btn:
                if st.button(f"雇用する", key=f"buy_{s_id}"):
                    if st.session_state.assets >= staff["cost"]:
                        st.session_state.assets -= staff["cost"]
                        st.session_state.staff[s_id]["count"] += 1
                        st.session_state.staff[s_id]["cost"] = int(staff["cost"] * 1.15)
                        st.rerun()
                    else:
                        st.error("資金が不足しています。")

    # PAGE 3: 新商品開発
    with tab3:
        st.subheader("プロダクト / イノベーション")
        for p_id, prod in st.session_state.products.items():
            col_info, col_btn = st.columns([3, 1])
            with col_info:
                status_txt = "【開発完了】" if prod["done"] else f"費用: ￥{prod['cost']:,}"
                st.markdown(f"**{prod['name']}** ({status_txt})<br><span style='color:#aaa;'>生産力ボーナス: 全体労働力 {prod['multi']} 倍</span>", unsafe_allow_html=True)
            with col_btn:
                if prod["done"]:
                    st.write("✅ 投資済み")
                else:
                    if st.button(f"開発投資", key=f"prod_{p_id}"):
                        if st.session_state.assets >= prod["cost"]:
                            st.session_state.assets -= prod["cost"]
                            st.session_state.products[p_id]["done"] = True
                            st.rerun()
                        else:
                            st.error("資金が不足しています。")

    # PAGE 4: 株価専用窓口
    with tab4:
        st.subheader("証券取引・企業価値レイアウト")
        st.write("会社の業績に応じてリアルタイムに自動変動します。")
        
        market_cap = stock_price * 10000
        rank = "E"
        if stock_price > 5000: rank = "S"
        elif stock_price > 2000: rank = "A"
        elif stock_price > 1000: rank = "B"
        elif stock_price > 500: rank = "C"
        elif stock_price > 200: rank = "D"
        
        sc1, sc2 = st.columns(2)
        with sc1:
            st.metric(label="仮想時価総額評価", value=f"￥{market_cap:,}")
        with sc2:
            st.metric(label="企業格付ランク", value=rank)

    # PAGE 5: 世界の市場記録
    with tab5:
        st.subheader("グローバルマーケット・レコード")
        
        display_count = 0
        for comp_id, comp in list(st.session_state.competitors.items()):
            if comp_id == st.session_state.company_id:
                continue
            display_count += 1
            
            col_c_info, col_c_btn = st.columns([3, 1])
            with col_c_info:
                st.markdown(f"<strong style='color:#ff4444;'>{comp['name']}</strong> (CEO: {comp['ceo']})<br>資産: ￥{comp['assets']:,} | 株価: ￥{comp['stockPrice']:,} | 防衛力: {comp['defense']} DEF", unsafe_allow_html=True)
            with col_c_btn:
