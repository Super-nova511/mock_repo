from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/health")
def home():
    return "Working"

@app.route("/")
def download():
    path = "messs5.zip"  # Your ZIP file
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
