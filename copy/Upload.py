# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
  return "<h1>これは論文掲載サービスです。</h1><h2>現在の掲載数は6つです。</h2>"
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
