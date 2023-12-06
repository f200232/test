from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "20F-0232 | 20F-0141 | 20F-1103 "


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.7.0.1', port=port)
