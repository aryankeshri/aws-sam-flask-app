from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    print("Hello")
    return jsonify(message='Hello from Flask on AWS Lambda!')

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()