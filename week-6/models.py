import sys
from unicodedata import name
sys.path.append("D:\Anaconda3\Lib\site-packages")
import mysql.connector
from mySQL import MySQLPassword

mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password=MySQLPassword(),
        database="mydatabase"
    )
mycursor=mydb.cursor()

def check_username(username):
    sql="SELECT username FROM member WHERE username =%s"
    val=(username)
    mycursor.execute(sql, (val,))
    result=mycursor.fetchall()
    return result

def insert_signupinfo(new_name, username_check, new_pwd):
    sql="INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    val=(new_name, username_check, new_pwd)
    mycursor.execute(sql, val)
    mydb.commit()

def check_signin(username):
    sql="SELECT * FROM member WHERE username =%s"
    val=(username)
    mycursor.execute(sql, (val,))
    result=mycursor.fetchone()
    return result

def create_msg(member_id, content):
    sql="INSERT INTO message (member_id, content) VALUES (%s, %s)"
    val=(member_id, content)
    mycursor.execute(sql, val)
    mydb.commit()

def get_msgs():
    sql="SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY time DESC"
    mycursor.execute(sql)
    msgs=mycursor.fetchall()
    return msgs