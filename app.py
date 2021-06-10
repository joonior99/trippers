import os

from bson import ObjectId
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
        user_info = db.users.find_one({"userid": payload["id"]}, {"_id": False})
        username = user_info["username"]

        posts_data = list(db.posts.find({}).sort("date", 1))
        posts = []
        for post in posts_data:
            post["_id"] = str(post["_id"])
            posts.append(post)
        return render_template('mainpage.html', username=username, posts=posts)
        # return render_template("mainpage.html")
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


@app.route("/posting", methods=["POST"])
def posting():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    title_receive = request.form["title_give"]
    comment_receive = request.form["comment_give"]
    date_receive = request.form["date_give"]
    file = request.files["file_give"]

    user_info = db.users.find_one({"userid": payload["id"]})
    username = user_info["username"]
    userid = user_info["userid"]

    extension = file.filename.split(".")[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f"file-{mytime}"
    save_to = f"static/img/{filename}.{extension}"
    file.save(save_to)

    doc = {
        "img_file": f"{filename}.{extension}",
        "username": username,
        "userid": userid,
        "title": title_receive,
        "comment": comment_receive,
        "date": date_receive
    }
    db.posts.insert_one(doc)
    return jsonify({"msg": "등록 완료"})


@app.route("/get_posts", methods=["GET"])
def get_posts():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        posts = list(db.posts.find({}).sort("date", -1).limit(20))
        for post in posts:
            post["_id"] = str(post["_id"])
        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "posts": posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route("/deleteCard", methods=["DELETE"])
def delete_card():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    user_info = db.users.find_one({"userid": payload["id"]})
    userid = user_info["userid"]

    id_value_receive = request.form["id_value_give"]
    author_info = db.posts.find_one({"_id": ObjectId(id_value_receive)})
    author_id = author_info["userid"]
    file_name = author_info["img_file"]

    if userid == author_id:
        db.posts.delete_one({"_id": ObjectId(id_value_receive)})
        os.remove("static/img/" + file_name)
        return jsonify({"msg": "삭제완료!"})
    else:
        return jsonify({"msg": "삭제 권한이 없습니다."})



@app.route("/update", methods=["POST"])
def update():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    # 로그인 계정 정보
    user_info = db.users.find_one({"userid": payload["id"]})
    userid = user_info["userid"]

    # 게시물에 대한 정보
    id_value_receive = request.form["id_value_give"]
    author_info = db.posts.find_one({"_id": ObjectId(id_value_receive)})
    author_id = author_info["userid"]

    data = db.posts.find_one({"_id": ObjectId(id_value_receive)})
    title = data["title"]
    comment = data["comment"]
    file_name = data["img_file"]

    if userid == author_id:
        return jsonify({"result": "success", "title": title, "comment": comment, "file_name": file_name})
    else:
        return jsonify({"msg": "수정 권한이 없습니다."})


@app.route("/modify_card", methods=["POST"])
def modify_card():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    id_value_receive = request.form["id_value_give"]
    author_info = db.posts.find_one({"_id": ObjectId(id_value_receive)})
    file_name = author_info["img_file"]

    title_receive = request.form["title_give"]
    comment_receive = request.form["comment_give"]
    file = request.files.get("file_give")

    today = datetime.now()

    doc = {
        "title": title_receive,
        "comment": comment_receive,
        "date": today.strftime('%Y.%m.%d.%H.%M.%S')
    }

    if file is not None:
        os.remove("static/img/" + file_name)
        extension = file.filename.split(".")[-1]
        mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
        filename = f"file-{mytime}"
        save_to = f"static/img/{filename}.{extension}"
        file.save(save_to)
        doc["img_file"] = f"{filename}.{extension}"

    db.posts.update_one({"_id": ObjectId(id_value_receive)}, {"$set": doc})
    return jsonify({"msg": "수정완료!"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
