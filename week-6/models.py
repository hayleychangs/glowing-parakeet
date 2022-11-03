import sys
from unicodedata import name
sys.path.append("D:\Anaconda3\Lib\site-packages")
import mysql.connector
from mySQL import MySQLPassword

dbconfig={
    "host":"localhost",
    "port":"3306",
    "database":"mydatabase",
    "user":"root",
    "password":MySQLPassword(),
}
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 2,
                                                      **dbconfig)
cnx=cnxpool.get_connection()
mycursor=cnx.cursor()

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
    cnx.commit()

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
    cnx.commit()


def get_msgs():
    sql="SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY time DESC"
    mycursor.execute(sql)
    msgs=mycursor.fetchall()
    return msgs




# mydb=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password=MySQLPassword(),
#         database="mydatabase"
#     )