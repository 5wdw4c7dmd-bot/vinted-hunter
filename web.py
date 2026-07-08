from flask import Flask
from status import status

app = Flask(__name__)

@app.route("/")
def home():

    return f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Pokémon Hunter</title>

<style>

body {{

    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:0;
    padding:20px;

}}

.card {{

    max-width:600px;
    margin:auto;

    background:white;

    border-radius:15px;

    padding:25px;

    box-shadow:0 10px 25px rgba(0,0,0,.15);

}}

h1{{margin-top:0}}

.item{{
    padding:12px 0;
    border-bottom:1px solid #eee;
}}

.value{{
    font-size:22px;
    font-weight:bold;
}}

.green{{
    color:#27ae60;
}}

</style>

</head>

<body>

<div class="card">

<h1>🟢 Pokémon Hunter</h1>

<div class="item">
Bot<br>
<span class="value green">
{"🟢 Running" if status["running"] else "🔴 Stopped"}
</span>
</div>

<div class="item">
Kontrol<br>
<span class="value">
{status["checks"]}
</span>
</div>

<div class="item">
Alertů<br>
<span class="value">
{status["alerts"]}
</span>
</div>

<div class="item">
Poslední kontrola<br>
<span class="value">
{status["last_check"]}
</span>
</div>

<div class="item">
Poslední produkt<br>
<span class="value">
{status["last_product"]}
</span>
</div>

<div class="item">
Cena<br>
<span class="value">
{status["last_price"]} Kč
</span>
</div>

<div class="item">
SCORE<br>
<span class="value">
⭐ {status["last_score"]}
</span>
</div>

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=False,
    )