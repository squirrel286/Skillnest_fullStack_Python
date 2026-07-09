from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "YARAAAAA"

@app.route("/nosotros")
def nosotros():
    return "<h1>Conócenos un poco más!</h1>"
#Productos

@app.route("/productos")
def productos():
    return "<h1>Productos disponibles pronto...</h1>"
#Contacto

@app.route("/contacto")
def contacto():
    return "<h1>Contáctanos en xxxxx@gmail.com</h1>"
if __name__ == "__main__":
    app.run(debug=True)