import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return '<h2>Welcome! Go to /download to download the ZIP file.</h2>'

@app.route("/download")
def download():
    return send_file("messs5.zip", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
