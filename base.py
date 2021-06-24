from flask import Flask,jsonify,request
from nlp_pos_extract import nlp_it
import json

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
    response = app.response_class(
        response=json.dumps(nlp_it(dictate), separators=(',', ':')),
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
