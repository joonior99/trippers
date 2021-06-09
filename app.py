from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

SECRET_KEY = 'TRIPPERS'

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbtrippers


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        return render_template("mainpage.html")
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.route("/sign_up/save", methods=["POST"])
def sign_up():
    username_receive = request.form["username_give"]
    userid_receive = request.form["userid_give"]
    userpw_receive = request.form["userpw_give"]
    userpw_hash = hashlib.sha256(userpw_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "userid": userid_receive,
        "userpw": userpw_hash
    }
    db.users.insert_one(doc)
    return jsonify({"result": "success"})


@app.route("/sign_in", methods=["POST"])
def sign_in():
    userid_receive = request.form["userid_give"]
    userpw_receive = request.form["userpw_give"]

    pw_hash = hashlib.sha256(userpw_receive.encode('utf-8')).hexdigest()
    uname = db.users.find_one({"userid": userid_receive}, {"_id": False})
    username = uname["username"]
    result = db.users.find_one({"userid": userid_receive, "userpw": pw_hash})

    if result is not None:
        payload = {
            'id': userid_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        return jsonify({'result': 'success', 'token': token, 'username': username})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route("/write_review")
def write_review():
    return render_template("review.html")

@app.route("/go_main")
def go_main():
    return render_template("mainpage.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
