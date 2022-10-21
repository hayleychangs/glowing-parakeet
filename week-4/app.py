from email import message
import sys
import secrets
from urllib import response
sys.path.append("D:\Anaconda3\Lib\site-packages")
from flask import Flask, request, render_template, redirect, url_for, make_response
#from datatime import timedelta

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static",
) 

key = secrets.token_urlsafe(16)
app.secret_key="key"

#app.permanent_session_lifetime=timedelta(minutes=10)

@app.route("/")
def index():
    # resp=make_response(render_template("index.html"))
    # resp.set_cookie(key="SignInStatus", value="Not Signed In")
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    if request.method=="POST":
        #session.permanent=True
        if request.form["username"]=="test" and request.form["password"]=="test":
            resp=make_response(redirect(url_for("member")))
            resp.set_cookie(key="SignInStatus", value="Signed In successfully")
            return resp
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
    SignInStatus=request.cookies.get("SignInStatus")
    if SignInStatus=="Signed In successfully":
        return render_template("member.html")
    else:
        return redirect(url_for("index"))

@app.route("/error")
def error():
    errorMessage=request.args.get("message","")
    return  render_template("error.html", text=errorMessage)

@app.route("/signout", methods=["GET"])
def signout():
    resp=make_response(redirect(url_for("index")))
    resp.delete_cookie(key="SignInStatus")
    return resp

@app.route("/square/<integer>")
def square(integer):
    result=int(integer)*int(integer)
    return render_template("square.html",answer=result)

if __name__=="__main__":
    app.run(port=3000)






# @app.route("/calculate",methods=["GET","POST"])
# def calculate():
#     if request.method=="POST":
#         return redirect(url_for("square", integer=request.form.get("integer")))
#     return render_template("index.html")
