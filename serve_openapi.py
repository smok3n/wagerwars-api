from flask import Flask, send_file

app = Flask(__name__)

@app.route("/openapi.json")
def openapi():
    return send_file("wagerwars_openapi.json", mimetype="application/json")

@app.route("/")
def home():
    return '<h1>WagerWars API</h1><p>OpenAPI spec available at <a href="/openapi.json">/openapi.json</a></p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
