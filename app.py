from flask import Flask, request, redirect

app = Flask(__name__)

ENTRY_PASSWORD = "deeptacos"
FINAL_WORD = "裏庭タコス"

STYLE = """
<style>
body {
    background:#0a0a0a;
    color:#eaeaea;
    font-family: 'Noto Sans JP', sans-serif;
    text-align:center;
    padding-top:20vh;
    animation: fade 1s ease;
}
@keyframes fade {
  from {opacity:0;}
  to {opacity:1;}
}
h2 {
    font-weight:300;
    letter-spacing:2px;
}
a, input[type="submit"] {
    display:block;
    margin:20px auto;
    padding:10px 20px;
    width:220px;
    text-decoration:none;
    color:#eaeaea;
    border:1px solid #444;
    background:none;
}
a:hover, input[type="submit"]:hover {
    border-color:#ff4444;
    color:#ff4444;
}
input {
    background:none;
    border:1px solid #444;
    color:#eaeaea;
    padding:10px;
    width:220px;
    text-align:center;
    margin-top:20px;
}
body::after {
    content:"";
    position:fixed;
    top:0; left:0;
    width:100%;
    height:100%;
    background:url('https://www.transparenttextures.com/patterns/asfalt-dark.png');
    opacity:0.2;
    pointer-events:none;
}
</style>
"""

# 入口
@app.route("/")
def lock():
    return STYLE + """
    <h2>ここは閉じてる</h2>
    <p>……合言葉は？</p>
    <form action="/unlock">
        <input name="pw">
        <input type="submit" value="開ける">
    </form>
    """

@app.route("/unlock")
def unlock():
    if request.args.get("pw") == ENTRY_PASSWORD:
        return redirect("/start")
    return STYLE + "<h2>違う。帰れ。</h2><a href='/'>戻る</a>"

# スタート
@app.route("/start")
def start():
    return STYLE + """
    <h2>匂いはする</h2>
    <p>でも全員のためじゃない</p>
    <a href="/step1">進む</a>
    <a href="/end">帰る</a>
    """

# 違和感
@app.route("/step1")
def step1():
    return STYLE + """
    <h2>足音が一つ多い気がする</h2>
    <a href="/fail1">振り返る</a>
    <a href="/step2">無視する</a>
    """

@app.route("/fail1")
def fail1():
    return STYLE + """
    <h2>余計なことするやつは向いてない</h2>
    <a href="/">最初に戻る</a>
    """

# 接触前
@app.route("/step2")
def step2():
    return STYLE + """
    <h2>煙の奥に、誰かいる</h2>
    <a href="/fail2">声をかける</a>
    <a href="/fail2">近づく</a>
    <a href="/step3">待つ</a>
    """

@app.route("/fail2")
def fail2():
    return STYLE + """
    <h2>勝手に動くな</h2>
    <p>帰れ</p>
    <a href="/">最初に戻る</a>
    """

# 店主
@app.route("/step3")
def step3():
    return STYLE + """
    <h2>……気づいてるなら言え</h2>
    <p>何しに来た</p>
    <form action="/step4">
        <input name="reason">
        <input type="submit" value="答える">
    </form>
    """

@app.route("/step4")
def step4():
    reason = request.args.get("reason")
    if reason and ("食" in reason or "探" in reason):
        return STYLE + """
        <h2>……いい</h2>
        <p>最後だ。合言葉は？</p>
        <form action="/result">
            <input name="word">
            <input type="submit" value="送信">
        </form>
        """
    return STYLE + "<h2>目的が曖昧だな。帰れ。</h2><a href='/'>最初に戻る</a>"

# 最終
@app.route("/result")
def result():
    if request.args.get("word") == FINAL_WORD:
        return STYLE + """
        <h2>……いい。入れ。</h2>
        <p>その画面、見せろ</p>
        <p>裏メニュー『深層タコス』解放</p>
        """
    return STYLE + "<h2>違う。帰れ。</h2><a href='/'>最初に戻る</a>"

@app.route("/end")
def end():
    return STYLE + """
    <h2>その判断、嫌いじゃない</h2>
    <p>また来い</p>
    <a href="/">戻る</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    