import streamlit as st
import streamlit.components.v1 as components

# Streamlitのページ設定（タイトルとレイアウト）
st.set_page_config(page_title="Corporate Wars Online", layout="wide")

# HTML/CSS/JavaScriptのコードを文字列として定義
html_code = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Wars Online</title>
    <style>
        body { font-family: 'Helvetica Neue', Arial, sans-serif; background: #1a1a1a; color: #fff; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1, h2 { color: #00ffcc; border-bottom: 2px solid #333; padding-bottom: 10px; }
        .card { background: #2a2a2a; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        input, button { width: 100%; padding: 12px; margin: 8px 0; border-radius: 4px; border: none; box-sizing: border-box; font-size: 16px; }
        input { background: #3a3a3a; color: #fff; }
        button { background: #00ffcc; color: #1a1a1a; font-weight: bold; cursor: pointer; transition: 0.2s; }
        button:hover { background: #00cca3; }
        button.attack { background: #ff4444; color: #fff; }
        button.attack:hover { background: #cc3333; }
        .flex { display: flex; justify-content: space-between; gap: 10px; }
        .market-list { list-style: none; padding: 0; }
        .market-item { background: #333; padding: 15px; margin-bottom: 10px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; border-left: 5px solid #00ffcc; }
        .market-item.enemy { border-left-color: #ff4444; }
        .share-uri { background: #111; padding: 10px; border-radius: 4px; word-break: break-all; font-family: monospace; font-size: 12px; color: #aaa; margin-top: 10px; }
    </style>
</head>
<body>

<div class="container">
    <h1>Corporate Wars Online</h1>

    <!-- 1. 会社設立・ログイン画面 -->
    <div id="setup-screen" class="card">
        <h2>会社を設立する</h2>
        <input type="text" id="company-name" placeholder="会社名を入力してください">
        <input type="text" id="ceo-name" placeholder="CEO（あなたの名前）">
        <button onclick="createCompany()">登記申請（ゲーム開始）</button>
    </div>

    <!-- 2. メインゲーム画面 -->
    <div id="game-screen" class="card" style="display:none;">
        <h2 id="display-company">株式会社 ---</h2>
        <p>CEO: <span id="display-ceo">---</span></p>
        
        <div class="card" style="background:#222;">
            <div class="flex">
                <div>現在の総資産:<br><strong style="font-size: 24px; color: #00ffcc;">￥<span id="display-assets">0</span></strong></div>
                <div>会社の防衛力:<br><strong style="font-size: 24px; color: #ffcc00;"><span id="display-defense">100</span> DEF</strong></div>
            </div>
        </div>

        <div class="flex">
            <button onclick="work()">営業活動（資金を稼ぐ）</button>
            <button onclick="upgradeDefense()">セキュリティ強化（防衛+50 / ￥500）</button>
        </div>

        <button onclick="generateShareLink()" style="background:#555; color:#fff; margin-top:15px;">同期用リンクを生成してコピー</button>
        <div id="share-area" style="display:none;">
            <p style="font-size:12px; margin-bottom:2px;">このURLを相手に渡すか、相手のURLをブラウザで開くと市場が繋がります：</p>
            <div class="share-uri" id="share-url"></div>
        </div>
    </div>

    <!-- 3. オンライン競合会社市場 -->
    <div id="market-screen" class="card" style="display:none;">
        <h2>世界の市場（競合他社一覧）</h2>
        <p style="font-size:12px; color:#aaa;">※競合の防衛力を0にすると、その資産をすべて奪い取って買収できます。</p>
        <ul id="market-list" class="market-list"></ul>
    </div>
</div>

<script>
    let myCompany = { id: "", name: "", ceo: "", assets: 1000, defense: 100 };
    let competitors = {};

    window.onload = function() {
        // Streamlit環境（iframe内）の親ウィンドウのURLからデータパラメータを取得
        const parentUrl = (window.location != window.parent.location) ? document.referrer : document.location.href;
        const urlObj = new URL(parentUrl);
        const params = urlObj.searchParams;

        if (params.has("data")) {
            try {
                const decoded = JSON.parse(decodeURIComponent(atob(params.get("data"))));
                Object.keys(decoded).forEach(id => { competitors[id] = decoded[id]; });
                updateMarketUI();
            } catch(e) { console.error("データ同期失敗", e); }
        }
        
        if (localStorage.getItem("my_company")) {
            myCompany = JSON.parse(localStorage.getItem("my_company"));
            showGame();
        }
    }

    function createCompany() {
        const name = document.getElementById("company-name").value.trim();
        const ceo = document.getElementById("ceo-name").value.trim();
        if (!name || !ceo) return alert("会社名とCEO名を入力してください");

        myCompany.id = "comp_" + Math.random().toString(36).substring(2, 9);
        myCompany.name = name;
        myCompany.ceo = ceo;
        myCompany.assets = 1000;
        myCompany.defense = 100;

        saveAndRefresh();
        showGame();
    }

    function showGame() {
        document.getElementById("setup-screen").style.display = "none";
        document.getElementById("game-screen").style.display = "block";
        document.getElementById("market-screen").style.display = "block";
        updateUI();
    }

    function saveAndRefresh() {
        localStorage.setItem("my_company", JSON.stringify(myCompany));
        updateUI();
    }

    function updateUI() {
        document.getElementById("display-company").innerText = myCompany.name;
        document.getElementById("display-ceo").innerText = myCompany.ceo;
        document.getElementById("display-assets").innerText = myCompany.assets.toLocaleString();
        document.getElementById("display-defense").innerText = myCompany.defense;
        
        competitors[myCompany.id] = myCompany;
        updateMarketUI();
    }

    function work() {
        const gain = Math.floor(Math.random() * 150) + 50;
        myCompany.assets += gain;
        saveAndRefresh();
    }

    function upgradeDefense() {
        if (myCompany.assets < 500) return alert("資金が足りません（500円必要）");
        myCompany.assets -= 500;
        myCompany.defense += 50;
        saveAndRefresh();
    }

    function updateMarketUI() {
        const listEl = document.getElementById("market-list");
        listEl.innerHTML = "";

        Object.keys(competitors).forEach(id => {
            if (id === myCompany.id) return;

            const comp = competitors[id];
            const li = document.createElement("li");
            li.className = "market-item enemy";
            li.innerHTML = `
                <div>
                    <strong>\${comp.name}</strong> (CEO: \${comp.ceo})<br>
                    資産: ￥\${comp.assets.toLocaleString()} / 防衛力: \${comp.defense} DEF
                </div>
                <div>
                    <button class="attack" onclick="attackCompany('\${id}')">買収攻撃</button>
                </div>
            `;
            listEl.appendChild(li);
        });
    }

    function attackCompany(targetId) {
        if (myCompany.assets < 300) return alert("攻撃資金が足りません（1回300円必要）");
        
        myCompany.assets -= 300;
        const target = competitors[targetId];
        const damage = Math.floor(Math.random() * 40) + 10;

        target.defense -= damage;

        if (target.defense <= 0) {
            alert(`【買収成功！】 \${target.name} を完全に買収しました！相手の全資産 ￥\${target.assets.toLocaleString()} を吸収します。`);
            myCompany.assets += target.assets;
            delete competitors[targetId];
        } else {
            alert(`\${target.name} に買収攻撃を仕掛け、防衛力を \${damage} 削りました！ (残りDEF: \${target.defense})`);
        }

        saveAndRefresh();
    }

    function generateShareLink() {
        competitors[myCompany.id] = myCompany;
        const jsonStr = JSON.stringify(competitors);
        const encodedData = btoa(encodeURIComponent(jsonStr));
        
        const parentUrl = (window.location != window.parent.location) ? document.referrer : document.location.href;
        const urlObj = new URL(parentUrl);
        
        const shareUrl = urlObj.origin + urlObj.pathname + "?data=" + encodedData;
        
        document.getElementById("share-url").innerText = shareUrl;
        document.getElementById("share-area").style.display = "block";
        
        navigator.clipboard.writeText(shareUrl).then(() => {
            alert("同期用URLをコピーしました！友達に共有してください。");
        });
    }
</script>

</body>
</html>
"""

# Streamlit上でHTMLコンポーネントを実行（画面いっぱいに表示）
components.html(html_code, height=900, scrolling=True)
