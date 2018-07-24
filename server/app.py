from flask import Flask, request, jsonify
from sklearn import datasets, svm
from sklearn.externals import joblib

import os
import argparse

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False 
clf = None
args = None

@app.route("/", methods=['GET'])
def index():
    return "Hello, scikit learn!"

@app.route("/reload", methods=['GET'])
def reload():
    clf = joblib.load(args.model)
    return "model reload success."


@app.route("/predict", methods=['POST'])
def predict():
    if request.headers['Content-Type'] != 'application/json':
        print(request.header['Content-Type'])    
        return jsonify(res='error'), 400

    if clf is None:
        raise Exception("The scikit model is not loaded.")

    data = clf.predict(request.json)

    return jsonify({'result':data.tolist()})

def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description='Flask Server for scikit-learn')
    parser.add_argument(
        '--model',
        default=os.environ.get('MODEL_FILE'),
        required=False,
        help='scikit model file')
    parser.add_argument(
        '--host',
        default="0.0.0.0",
        required=False,
        help='bind host ip address')
    parser.add_argument(
        '--port',
        type=int,
        default=os.environ.get('SCIKIT_SERVER_PORT'),
        required=False,
        help='bind host port number')
    parser.add_argument(
        '--debug',
        default=False,
        action='store_true',
        help='server run debug mode')

    return parser.parse_args()

def main():
    global clf
    global args

    args = parse_command_line_args()
    clf = joblib.load(args.model)

    port = args.port
    if port is None:
        port = 5000

    app.run(debug=args.debug, host=args.host, port=port)


if __name__ == "__main__":
    main()