from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('name.html', message="数字を入力してください。")

@app.route('/result', methods=["POST"])
def suji_to_kansuji():
    # POST送信の処理
    num = request.form["field"]
    try:
        int(num)
        suji   = ["","壱","弐","参","四","五","六","七","八","九"]
        kugiri = ["","拾","百","千"]
        tani   = ["","万","億","兆"]
#str(num)で数字を文字列にしlist()でリスト化している
#mapで文字列のリストをint型に変換→それをリストに入れる
        num  = list(map(int,list(str(num))))
        kansuji = []
#lenでリストの長さを、rangeで連続した数値を取得
#zipで複数のリストの要素を取得
        for m, n in zip(range(len(num)), reversed(num)) :
            keta = []
            if m%4 == 0:
                keta+=[suji[n],tani[m//4]]
            elif m%4 == 1 and n>0:
                keta+=[suji[n],kugiri[m%4]]
            elif m%4 == 2 and n>0:
                keta+=[suji[n],kugiri[m%4]]
            elif m%4 == 3 and n>0:
                keta+=[suji[n],kugiri[m%4]]
    #joinを使ってリストを連結
            kansuji.append("".join(keta))

        kansuji = "".join(reversed(kansuji))

        return render_template('mainpage.php', message = "漢数字に変換＝{}".format(kansuji))

    except ValueError:
        error = 204
        return render_template('mainpage.php', message = "{}".format(error))

if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=8888, debug=True)
