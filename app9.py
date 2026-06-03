import streamlit as st
import random
import time

# 1. ページ基本設定
st.set_page_config(page_title="Corporate Wars Premium", layout="wide")

st.markdown("""
<style>
    body { background-color: #121212; color: #e0e0e0; }
    h1 { color: #00ffcc !important; text-align: center; font-family: 'Helvetica Neue', Arial, sans-serif; }
    .stButton>button { width: 100%; border-radius: 4px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🏢 Corporate Wars Premium (Fully Online Cloud Edition)")

# =================================================================
# 全員で共有する「クラウド仮想市場データベース」の構築
# =================================================================
if "GLOBAL_MARKET_DATABASE" not in st.session_state.__class__.__dict__:
    st.session_state.__class__.GLOBAL_MARKET_DATABASE = {}

GLOBAL_MARKET = st.session_state.__class__.GLOBAL_MARKET_DATABASE


# 2. 個人セッションデータの初期化
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


# クラウドデータベースへのデータ同期関数
def sample_sync_to_cloud(stock_price_current):
    if not st.session_state.company_name:
        return
    GLOBAL_MARKET[st.session_state.company_id] = {
        "name": st.session_state.company_name,
        "ceo": st.session_state.ceo_name,
        "assets": st.session_state.assets,
        "defense": st.session_state.defense,
        "stockPrice": stock_price_current,
        "last_update": time.time()
    }

def sample_sync_from_cloud():
    if st.session_state.company_id in GLOBAL_MARKET:
        cloud_data = GLOBAL_MARKET[st.session_state.company_id]
        if cloud_data["defense"] <= 0:
            st.error(f"🚨 【M&A警告】あなたの会社は競合他社によって完全に買収合併されました！資産がリセットされます。")
            st.session_state.company_name = ""
            st.session_state.ceo_name = ""
            st.session_state.assets = 2000
            st.session_state.defense = 100
            st.session_state.debt = 0
            st.session_state.subsidiaries = []
            for s_id in st.session_state.staff: st.session_state.staff[s_id]["count"] = 0
            for p_id in st.session_state.products: st.session_state.products[p_id]["done"] = False
            if st.session_state.company_id in GLOBAL_MARKET:
                del GLOBAL_MARKET[st.session_state.company_id]
            st.rerun()
        else:
            st.session_state.defense = cloud_data["defense"]


# --- 4. 未ログイン画面（会社設立） ---
if not st.session_state.company_name:
    st.subheader("新規企業の創立登記申請")
    st.info("会社を設立すると、自動的に「共通オンライン市場」へ同期され、他のプレイヤーの画面にあなたの会社が勝手に出現します。コード交換は一切不要です！")
    
    input_corp = st.text_input("新しい会社名", key="init_corp", placeholder="クリスタル株式会社")
    input_ceo = st.text_input("代表取締役CEO（あなたの名前）", key="init_ceo", placeholder="クロダイ")
    
    if st.button("会社を設立して市場に参入する", type="primary"):
        if input_corp.strip() and input_ceo.strip():
            st.session_state.company_id = f"corp_{random.randint(100000, 999999)}"
            st.session_state.company_name = input_corp.strip()
            st.session_state.ceo_name = input_ceo.strip()
            st.session_state.last_tick = time.time()
            
            GLOBAL_MARKET[st.session_state.company_id] = {
                "name": st.session_state.company_name,
                "ceo": st.session_state.ceo_name,
                "assets": st.session_state.assets,
                "defense": st.session_state.defense,
                "stockPrice": 100,
                "last_update": time.time()
            }
            st.success("市場への自動登記が完了しました！")
            st.rerun()
        else:
            st.error("すべての項目を入力してください。")

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
    
    sample_sync_from_cloud()
    sample_sync_to_cloud(stock_price)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="自社総資産", value=f"￥{st.session_state.assets:,}")
    col2.metric(label="自社現在株価", value=f"￥{stock_price:,}")
    col3.metric(label="グループ社員数 / 総生産力", value=f"{sum(s['count'] for s in st.session_state.staff.values())} 名 / {auto_power:,}秒")
    
    # 8つの独立したタブメニューを生成
    t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs([
        "🏢 自社概念", "💼 営業アクション", "🏢 子会社管理", 
        "👥 社員雇用", "🧪 新商品開発", "🏦 銀行窓口", 
        "📈 株価専用窓口", "⚔️ 世界の市場記録"
    ])
    
    # ★重要修正ポイント：すべての「with tx:」を完全に左揃えにし、ネスト（入れ子）を完全解消
    with t1:
        st.subheader("企業アイデンティティ")
        st.write(f"**会社名:** {st.session_state.company_name}（親会社）")
        st.write(f"**最高経営責任者 (CEO):** {st.session_state.ceo_name}")
        st.write(f"**ユニーク企業ID:** `{st.session_state.company_id}`")
        st.write(f"**保有子会社数:** {len(st.session_state.subsidiaries)} 社")
        st.write(f"**セキュリティ防衛力:** {st.session_state.defense} DEF")
        st.write(f"**現在の借金残高:** ￥{st.session_state.debt:,}")
        st.success("🟢 あなたの会社はクラウド共有サーバーへリアルタイム同期されています。コードのやり取りは不要です。")

    with t2:
        st.subheader("💼 コアビジネス・経営コマンド")
        st.write("時間を進めて売上を回収したり、会社の基礎防衛力を固めるページです。")
        act_box = st.container(border=True)
        c1, c2, c3 = act_box.columns(3)
        with c1:
            st.markdown("**【能動的営業】**", unsafe_allow_html=True)
            if st.button("営業活動を行う (+￥100)"):
                st.session_state.assets += 100
                sample_sync_to_cloud(stock_price)
                st.rerun()
        with c2:
            st.markdown("**【セキュリティ強化】**", unsafe_allow_html=True)
            if st.button("セキュリティを強化 (-￥1,000 / +100 DEF)"):
                if st.session_state.assets >= 1000:
                    st.session_state.assets -= 1000
                    st.session_state.defense += 100
                    sample_sync_to_cloud(stock_price)
                    st.rerun()
                else:
                    st.error("資金が不足しています。")
        with c3:
            st.markdown("**【最新データ更新】**", unsafe_allow_html=True)
            if st.button("市場データをリロード（売上回収・ライバル情報同期）"):
                st.rerun()

    with t3:
        st.subheader("🏢 子会社・グループ企業マネジメント")
        st.write("子会社を設立し、投資を行うことで、グループ全体の生産力（1秒あたりの売上）に強力な乗算ボーナスがかかります。")
        
        with st.expander("➕ 新しい子会社を設立する"):
            sub_name = st.text_input("子会社の社名")
            sub_type = st.selectbox("事業セクター", ["IT・ソフトウェア", "不動産・インフラ", "バイオ・先端医療", "宇宙開発"])
            capital = st.number_input("出資資本金（最低 ￥5,000）", min_value=5000, max_value=max(5000, st.session_state.assets), step=5000)
            if st.button("出資登記して子会社にする"):
                if st.session_state.assets < capital:
                    st.error("親会社の資金が足りません。")
                elif not sub_name.strip():
                    st.error("子会社の名前を入力してください。")
                else:
                    st.session_state.assets -= capital
                    st.session_state.subsidiaries.append({
                        "name": sub_name.strip(), "type": sub_type, "capital": capital, "level": 1, "invest_cost": int(capital * 0.8)
                    })
                    sample_sync_to_cloud(stock_price)
                    st.rerun()

        st.markdown("### 📊 保有子会社一覧")
        if not st.session_state.subsidiaries:
            st.info("子会社はありません。")
        for idx, sub in enumerate(st.session_state.subsidiaries):
            s_box = st.container(border=True)
