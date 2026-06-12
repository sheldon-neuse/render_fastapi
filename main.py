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
                    <td>イクイノックス</td>
                    <td>ルメール</td>
                </tr>
                <tr>
                    <td style="background-color: white;">2</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: black;">3</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: black;">4</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: red;">5</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: red;">6</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: blue;">7</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: blue;">8</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: yellow;">9</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: yellow;">10</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: green;">11</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: green;">12</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: orange;">13</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: orange;">14</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: orange;">15</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: pink;">16</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: pink;">17</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
                </tr>
                <tr>
                    <td style="background-color: pink;">18</td>
                    <td>ドウデュース</td>
                    <td>武豊</td>
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