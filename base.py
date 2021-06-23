from flask import Flask,jsonify,request
from nlp_pos_extract import nlp_it

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "username": "Raaj",
        "endpoint": "/",
    })

@app.route('/nlp',methods= ['POST'])
def nlp():
    dictate = str(request.args.get('dictate'))
    return jsonify(nlp_it(dictate))

if __name__ == "__main__":
    app.run(debug=True)
