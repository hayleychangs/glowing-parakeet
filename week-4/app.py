from email import message
import sys
sys.path.append("D:\Anaconda3\Lib\site-packages")
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
#from datatime import timedelta

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static",
) 
app.secret_key="12345678"

#app.permanent_session_lifetime=timedelta(minutes=10)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    if request.method=="POST":
        #session.permanent=True
        if request.form["username"]=="test" and request.form["password"]=="test":
            user=request.form["username"]
            pwd=request.form["password"]
            session["user"]=user
            session["pwd"]=pwd
            return redirect(url_for("member"))
        else:
            if request.form["username"] =="" or request.form["password"] =="":
                error="請輸入帳號、密碼"
                return redirect(url_for("error", message=error))
            
            else:
                if (request.form["username"] !="test" and not None) or (request.form["password"] !="test" and not None):
                    error="帳號、或密碼輸入錯誤"
                    print(request.form["username"],request.form["password"])
                    return redirect(url_for("error", message=error))            
    else:
        if "user" in session:
            return redirect(url_for("member"))
        return render_template("index.html")

@app.route("/member")
def member():
    if "user" in session:
        user = session["user"]
        return render_template("member.html")
    else:
        return redirect(url_for("index"))

@app.route("/error")
def error():
    errorMessage=request.args.get("message","")
    return  render_template("error.html", text=errorMessage)

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("user", None)
    return redirect(url_for("index"))

@app.route("/calculate",methods=["GET","POST"])
def calculate():
    if request.method=="POST":
        return redirect(url_for("square", integer=request.form.get("integer")))
    return render_template("index.html")

@app.route("/square/<integer>")
def square(integer):
    result=int(integer)*int(integer)
    return render_template("square.html",answer=result)

if __name__=="__main__":
    app.run(port=3000)