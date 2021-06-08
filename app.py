from flask import Flask, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtrippers


@app.route('/')
def main():
    return render_template("login.html")

@app.route('/membership')
def membership():
    return render_template('membership.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)