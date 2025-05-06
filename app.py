from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Adam Karl Sansan ,br> BSIT 3-2nd 25 ,<br> System Integration and Architecture 1 <br> Semi Final "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)