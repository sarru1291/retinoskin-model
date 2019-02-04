from flask import Flask
app = Flask(__name__)


@app.route('/api/test')
def hello():
    return "sarru"

if __name__ == '__main__':
    app.run(debug=True)