import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("alacs.txt", as_attachment=True)

@app.route("/health")
def download():
    return "Working"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


