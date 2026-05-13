<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>剣道昇段審査 穴埋め練習</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 20px; background: #f4f4f4; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1 { border-bottom: 2px solid #333; padding-bottom: 10px; }
        .question { margin-bottom: 30px; padding: 15px; border-left: 5px solid #2196F3; background: #e3f2fd; }
        .drop-zone { display: inline-block; width: 100px; height: 30px; border-bottom: 2px solid #333; margin: 0 5px; vertical-align: middle; text-align: center; background: #fff; }
        .word-bank { margin-top: 20px; padding: 15px; border: 1px dashed #ccc; display: flex; flex-wrap: wrap; gap: 10px; }
        .word { padding: 5px 15px; background: #fff; border: 1px solid #333; cursor: grab; border-radius: 4px; }
        .word:active { cursor: grabbing; }
        button { margin-top: 20px; padding: 10px 20px; background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>

<div class="container">
    <h1>剣道昇段審査 穴埋めドリル</h1>

    <!-- 第2問 -->
    <div class="question">
        <p><strong>問2. 剣道修錬の心構え</strong><br>
        剣道を正しく学び、心身を修錬して旺盛なる（ <span class="drop-zone" id="q2-1"></span> ）を養い、剣道の特性を通じて（ <span class="drop-zone" id="q2-2"></span> ）を尊び、（ <span class="drop-zone" id="q2-3"></span> ）を重んじ、（ <span class="drop-zone" id="q2-4"></span> ）を尽くして常に自己の修養につとめ、以って、国家社会を愛して広く人類の（ <span class="drop-zone" id="q2-5"></span> ）に寄与せんとするものである。</p>
        <div class="word-bank">
            <div class="word" draggable="true">気力</div>
            <div class="word" draggable="true">礼節</div>
            <div class="word" draggable="true">信義</div>
            <div class="word" draggable="true">誠意</div>
            <div class="word" draggable="true">平和繁栄</div>
        </div>
    </div>

    <!-- 第6問 -->
    <div class="question">
        <p><strong>問6. 一足一刀の間合について</strong><br>
        一足一刀の間合とは、一歩（ <span class="drop-zone" id="q6-1"></span> ）相手に打突を与え、一歩（ <span class="drop-zone" id="q6-2"></span> ）相手の打突をはずすことができる。いわゆる（ <span class="drop-zone" id="q6-3"></span> ）に強く、（ <span class="drop-zone" id="q6-4"></span> ）にも強い基本的な間合である。</p>
        <div class="word-bank">
            <div class="word" draggable="true">踏み込めば</div>
            <div class="word" draggable="true">退けば</div>
            <div class="word" draggable="true">攻め</div>
            <div class="word" draggable="true">守り</div>
        </div>
    </div>

    <button onclick="checkAnswers()">答え合わせ</button>
</div>

<script>
    const words = document.querySelectorAll('.word');
    const zones = document.querySelectorAll('.drop-zone');

    words.forEach(word => {
        word.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text', e.target.innerText);
        });
    });

    zones.forEach(zone => {
        zone.addEventListener('dragover', (e) => e.preventDefault());
        zone.addEventListener('drop', (e) => {
            e.preventDefault();
            const data = e.dataTransfer.getData('text');
            e.target.innerText = data;
            e.target.style.background = "#fff9c4";
        });
    });

    function checkAnswers() {
        alert("正解を確認して、自分の回答と照らし合わせてみましょう！\n\n問2: 気力、礼節、信義、誠意、平和繁栄\n問6: 踏み込めば、退けば、攻め、守り");
    }
</script>

</body>
</html>
