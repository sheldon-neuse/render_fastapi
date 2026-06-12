from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉 - 大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶- 凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶 - 小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶 - 大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]

    return omikuji_list[random.randrange(10)]

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1 style="background-color: yellow;">Sをください!!!!!<br>
            お願いします!!!!!</h1>
            <table border="1">
                <tr>
                    <th>馬番</th>
                    <th>馬名</th>
                    <th>騎手</th>
                </tr>
                <tr>
                    <td style="background-color: white;">1</td>
                    <td>ダノンデサイル</td>
                    <td>戸崎圭</td>
                </tr>
                <tr>
                    <td style="background-color: white;">2</td>
                    <td>ミュージアムマイル</td>
                    <td>D. レ</td>
                </tr>
                <tr>
                    <td style="background-color: black; color: white;">3</td>
                    <td>シュガークン</td>
                    <td>吉村誠</td>
                </tr>
                <tr>
                    <td style="background-color: black; color: white;">4</td>
                    <td>ミクニインスパイア</td>
                    <td>丹内祐</td>
                </tr>
                <tr>
                    <td style="background-color: red; color: white;">5</td>
                    <td>クロワデュノール</td>
                    <td>北村友一</td>
                </tr>
                <tr>
                    <td style="background-color: red; color: white;">6</td>
                    <td>ビザンチンドリーム</td>
                    <td>西村淳</td>
                </tr>
                <tr>
                    <td style="background-color: blue; color: white;">7</td>
                    <td>ファミリータイム</td>
                    <td>幸英明</td>
                </tr>
                <tr>
                    <td style="background-color: blue; color: white;">8</td>
                    <td>タガノデュード</td>
                    <td>高杉吏</td>
                </tr>
                <tr>
                    <td style="background-color: yellow; color: black;">9</td>
                    <td>コスモキュランダ</td>
                    <td>横山武</td>
                </tr>
                <tr>
                    <td style="background-color: yellow; color: black;">10</td>
                    <td>ジューンテイク</td>
                    <td>松山弘</td>
                </tr>
                <tr>
                    <td style="background-color: green; color: white;">11</td>
                    <td>シンエンペラー</td>
                    <td>坂井瑠</td>
                </tr>
                <tr>
                    <td style="background-color: green; color: white;">12</td>
                    <td>マイネルエンペラー</td>
                    <td>川田将</td>
                </tr>
                <tr>
                    <td style="background-color: orange; color: black;">13</td>
                    <td>シェイクユアハート</td>
                    <td>古川吉</td>
                </tr>
                <tr>
                    <td style="background-color: orange; color: black;">14</td>
                    <td>スティンガーグラス</td>
                    <td>岩田望</td>
                </tr>
                <tr>
                    <td style="background-color: orange; color: black;">15</td>
                    <td>マイユニバース</td>
                    <td>横山典</td>
                </tr>
                <tr>
                    <td style="background-color: pink; color: black;">16</td>
                    <td>メイショウタバル</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: pink; color: black;">17</td>
                    <td>レガレイラ</td>
                    <td>C. ル</td>
                </tr>
                <tr>
                    <td style="background-color: pink; color: black;">18</td>
                    <td>ミステリーウェイ</td>
                    <td>松本大</td>
                </tr>
            </table>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/horse")
async def give_horseTicket(horse):
    rand = random.randrange(2)
    if rand == 0:
        return {"response": f"サーバです。{horse}の馬券ですね。多分当たらないとおもいますけど。"}  # f文字列というPythonの機能を使っている
    else:
        return {"response": f"サーバです。{horse}の馬券ですね。最高の買い目ですね。"}