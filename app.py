from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Adam karl Sansan <br> BSIT-2A 2nd 25 <br> System Integration and Achitecture 1 <br> Semi Final Exam <br>"

if __name__ == '__main__':
    app.run(debug=True)