from io import BytesIO
from flask import Flask, render_template, request
import qrcode
from base64 import b64encode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])  # Fixed typo here
def gerarQR():
    memoria = BytesIO()
    data = request.form.get("link")  # Fixed variable name here
    img = qrcode.make(data)
    img.save(memoria)
    memoria.seek(0)

    base64_img = "data:image/png;base64," + b64encode(memoria.getvalue()).decode("ascii")  # Fixed typo here

    return render_template("index.html", data=base64_img)  # Fixed variable name here

if __name__ == "__main__":
    app.run(debug=True)

