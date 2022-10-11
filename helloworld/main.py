import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!\n"

if __name__  == "__main__":
    app.run(host="localhost", port=8080, debug=True)