from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('name.html', message="漢数字を入力してください。")

@app.route('/result', methods=["POST"])
def kansuji_to_suji():

    # POST送信の処理
    kanji = request.form["field"]
    try:

        SUJI = {suji: index for index, suji in enumerate('零壱弐参四五六七八九')}
    #enumerateのインデックスを1から始める
        KUGIRI = {kugiri: 10**index for index, kugiri in enumerate('拾百千', 1)}
        TANI = {tani: 10000**index for index, tani in enumerate('万億兆', 1)}

        small = middle = big = 0
        for c in kanji:
            if c in SUJI:
            #辞書の値からインデックス（数字）を抽出
                small = small * 10 + SUJI[c]
            elif c in KUGIRI:
                middle += small * KUGIRI[c]
                small = 0
            elif c in TANI:
                big += (small + middle) * TANI[c]
                small = middle = 0

        m = big + middle + small
        return render_template('mainpage.php', message = "数字に変換＝{}".format(m))

    except ValueError:
        error = 204
        return render_template('mainpage.php', message = "{}".format(error))

if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=8888, debug=True)
