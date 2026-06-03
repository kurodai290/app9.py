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

st.title("🏢 Corporate Wars Premium (Subsidiary Edition)")

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
if "debt" not in st.session_state:
    st.session_state.debt = 0
if "subsidiaries" not in st.session_state:
    st.session_state.subsidiaries = []
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
    product_multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            product_multiplier *= p["multi"]
            
    sub_multiplier = 1.0
    for sub in st.session_state.subsidiaries:
        sub_multiplier += (sub["level"] * 0.1)
        
    final_power = int(base_power * product_multiplier * sub_multiplier)
    st.session_state.assets += final_power * elapsed
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
    base_power = sum(s["count"] * s["power"] for s in st.session_state.staff.values())
    product_multiplier = 1.0
    for p in st.session_state.products.values():
        if p["done"]:
            product_multiplier *= p["multi"]
            
    sub_multiplier = 1.0
    for sub in st.session_state.subsidiaries:
        sub_multiplier += (sub["level"] * 0.1)
        
    auto_power = int(base_power * product_multiplier * sub_multiplier)
    
    sub_value_bonus = sum(sub["level"] * 5000 for sub in st.session_state.subsidiaries)
    net_assets = st.session_state.assets - st.session_state.debt + sub_value_bonus
    stock_base = (net_assets * 0.05) + (sum(s["count"] for s in st.session_state.staff.values()) * 50) + (sum(1 for p in st.session_state.products.values() if p["done"]) * 1000)
    stock_price = max(10, int(stock_base * random.uniform(0.97, 1.03)))
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="自社総資産", value=f"￥{st.session_state.assets:,}")
    col2.metric(label="自社現在株価", value=f"￥{stock_price:,}")
    col3.metric(label="グループ社員数 / 総生産力", value=f"{sum(s['count'] for s in st.session_state.staff.values())} 名 / {auto_power:,}秒")
    
    # 営業アクションを独立させた「8つのタブメニュー」
    tabs = st.tabs(["🏢 自社概念", "💼 営業アクション", "🏢 子会社管理", "👥 社員雇用", "🧪 新商品開発", "🏦 銀行窓口", "📈 株価専用窓口", "⚔️ 世界の市場記録"])
    
    # TAB 1: 自社概念
    with tabs[0]:
        st.subheader("企業アイデンティティ")
        st.write(f"**会社名:** {st.session_state.company_name}（親会社）")
        st.write(f"**最高経営責任者 (CEO):** {st.session_state.ceo_name}")
        st.write(f"**保有子会社数:** {len(st.session_state.subsidiaries)} 社")
        st.write(f"**セキュリティ防衛力:** {st.session_state.defense} DEF")
        st.write(f"**現在の借金残高:** ￥{st.session_state.debt:,}")
        
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

    # ★ NEW TAB 2: 営業アクション（完全独立ページ）
    with tabs[1]:
        st.subheader("💼 コアビジネス・経営コマンド")
        st.write("社長としての直接的な経営介入や、時間を進めて社員の売上を回収するページです。")
        
        act_box = st.container(border=True)
        act_box.markdown("### 🛠️ 執行アクション選択")
        
        c1, c2, c3 = act_box.columns(3)
        with c1:
            st.markdown("**【能動的営業】**<br><span style='color:#aaa;'>社長自ら商談に向かい、確実な現金を手に入れます。</span>", unsafe_allow_html=True)
            if st.button("営業活動を行う (+￥100)"):
                st.session_state.assets += 100
                st.rerun()
        with c2:
            st.markdown("**【セキュリティ強化】**<br><span style='color:#aaa;'>費用を投じて社内サーバーを強固にし、M&A攻撃に備えます。</span>", unsafe_allow_html=True)
            if st.button("セキュリティを強化 (-￥1,000 / +100 DEF)"):
                if st.session_state.assets >= 1000:
                    st.session_state.assets -= 1000
                    st.session_state.defense += 100
                    st.rerun()
                else:
                    st.error("資金が不足しています。")
        with c3:
            st.markdown("**【ターン経過処理】**<br><span style='color:#aaa;'>ブラウザの時間を進め、社員や子会社が稼いだ自動売上を今すぐ一括回収します。</span>", unsafe_allow_html=True)
            if st.button("画面をリロード（売上回収）"):
                st.rerun()

    # TAB 3: 子会社管理
    with tabs[2]:
        st.subheader("🏢 子会社・グループ企業マネジメント")
        st.write("子会社を設立し、投資を行うことで、グループ全体の生産力（1秒あたりの売上）に強力な乗算ボーナスがかかります。")
        
        with st.expander("➕ 新しい子会社を設立する"):
            sub_name = st.text_input("子会社の社名（例：サイバーコア・データサイエンス株式会社）")
            sub_type = st.selectbox("事業セクター", ["IT・ソフトウェア", "不動産・インフラ", "バイオ・先端医療", "宇宙開発"])
            capital = st.number_input("出資資本金（親会社の資産から差し引かれます / 最低 ￥5,000）", min_value=5000, max_value=max(5000, st.session_state.assets), step=5000)
            
            if st.button("出資登記して子会社にする"):
                if st.session_state.assets < capital:
                    st.error("親会社の資金（総資産）が出資額に満たないため設立できません。")
                elif not sub_name.strip():
                    st.error("子会社の名前を入力してください。")
                else:
                    st.session_state.assets -= capital
                    new_sub = {
                        "name": sub_name.strip(),
                        "type": sub_type,
                        "capital": capital,
                        "level": 1,
                        "invest_cost": int(capital * 0.8)
                    }
                    st.session_state.subsidiaries.append(new_sub)
                    st.success(f"🎉 100%子会社『{sub_name}』を設立しました！グループシナジーが向上します。")
                    st.rerun()

        st.markdown("### 📊 保有子会社一覧")
        if not st.session_state.subsidiaries:
            st.info("現在保有している子会社はありません。上のパネルから出資・設立しましょう。")
            
        for idx, sub in enumerate(st.session_state.subsidiaries):
            s_box = st.container(border=True)
            s_box.markdown(f"**🏢 {sub['name']}** [{sub['type']}]")
            s_box.write(f"・初期資本金: ￥{sub['capital']:,} | 企業規模ランク: **Lv.{sub['level']}**")
            s_box.write(f"・現在のグループ貢献度: **全体生産力 +{sub['level'] * 10}% ボーナス**")
