import sys
import secrets
from unicodedata import name
sys.path.append("D:\Anaconda3\Lib\site-packages")
from flask import Flask, request, render_template, redirect, session, url_for, jsonify, make_response
#from datatime import timedelta
from flask_cors import CORS
from models import check_username, insert_signupinfo, check_signin, create_msg, get_msgs, getmemberinfo, rename

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static",
)
app.config["JSON_AS_ASCII"] = False

key=secrets.token_urlsafe(16)
app.secret_key="key"

CORS(app)

#app.permanent_session_lifetime=timedelta(minutes=10)

@app.route("/api/member", methods=["GET", "PATCH"])
def apimember():
    if request.method=="PATCH":
        try:
            if "user" in session:
                request_data=request.get_json()
                name_input=request_data["name"]
                name_insession=session["name"]
                response=rename(name_input, name_insession)
                #如果要讓使用者連續改名，這邊要重設session["name"]
                #result=check_username(name_input)
                #newname_db=result[0][0]
                #print(newname_db)
                #session["name"]=newname_db
                return response
            else:
                request_data=request.get_json()
                unauthorized_error_message=True
                response=make_response(jsonify({"error":unauthorized_error_message}), 401)
                return response
        except:
            unexpected_error_message=True
            error_response=make_response(jsonify({"error":unexpected_error_message}))
            return error_response
    else:
        if request.method=="GET":
            try:
                if "user" in session:
                    username_input=request.args.get("username", None)
                    response=getmemberinfo(username_input)
                    return response
                else:
                    unauthorized_error_message=None
                    response=make_response(jsonify({"data":unauthorized_error_message}), 401)
                    return response
            except:   
                unexpected_error_message=None
                unexpected_error_response=make_response(jsonify({"data":unexpected_error_message}))
                return unexpected_error_response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    new_name=request.form["name-signup"]
    username_check=request.form["username-signup"]
    new_password=request.form["password-signup"]
    if request.method=="POST":
        result=check_username(username_check)
        if result==[] and new_name!="" and username_check!="" and new_password!="":
            insert_signupinfo(new_name, username_check, new_password)
            signedup_msg="註冊成功"
            return redirect(url_for("signedup", message=signedup_msg))
        else:
            if result is not None:
                username_db=result[0][0]
                print(username_db)
                if username_db==username_check:
                    error="帳號已經被註冊"
                    return redirect(url_for("error", message=error))
    else:
        return redirect(url_for("index"))

@app.route("/signedup")
def signedup():
    signedup_message=request.args.get("message")
    return  render_template("signedup.html", text=signedup_message)

@app.route("/signin", methods=["POST"])
def signin():
    username_check=request.form["username_signin"]
    password_check=request.form["password_signin"]
    if request.method=="POST":
        #session.permanent=True
        result=check_signin(username_check)
        if result is None or (username_check =="" or password_check ==""):
            error="請輸入帳號、密碼"
            return redirect(url_for("error", message=error))
        else:
            id_db=result[0]
            name_db=result[1]
            username_db=result[2]
            password_db=result[3]
            if username_check==username_db and password_check==password_db:
                user=username_check
                password=password_check
                session["id"]=id_db
                session["name"]=name_db
                session["user"]=user
                session["password"]=password
                return redirect(url_for("member"))
            else:
                error="帳號、或密碼輸入錯誤"
                return redirect(url_for("error", message=error))
    else:
        if "user" in session:
            return redirect(url_for("member"))
        return render_template("index.html")

@app.route("/member")
def member():
    if "user" in session:
        username_check=session["user"]
        password_check=session["password"]
        member_name=session.get("name")
        msgs=get_msgs()
        return render_template("member.html", name_text=member_name, msgs=msgs)
    else:
        return redirect(url_for("index"))

@app.route("/message", methods=["POST"])
def message():
    if "user" in session:
        member_id=session.get("id")
        content=request.form["msg-content"]
        create_msg(member_id, content)
        return redirect(url_for("member"))
    else:
        return redirect(url_for("index"))

@app.route("/error")
def error():
    error_message=request.args.get("message")
    return  render_template("error.html", text=error_message)

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("id", None)
    session.pop("name", None)
    session.pop("user", None)
    session.pop("password", None)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(port=3000)
