from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola "
    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)