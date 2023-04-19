from flask import Flask,render_template,jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/bye')
def bye():
    c = 2*534
    s = str(c)
    retJson = {
        'Name':'Ankush',
        'Age': 22,
        "phones" :[
            {
                "phoneName": "Iphone8",
                "phoneNumber": 11111
            },
            {
                "phoneName": "Nokia",
                "phoneNumber": 11121
            }
        ]

    }
    return jsonify(retJson)


if __name__ == "__main__":
    app.run(debug=True,port=5001)