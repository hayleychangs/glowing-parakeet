import sys
from unicodedata import name
sys.path.append("D:\Anaconda3\Lib\site-packages")
import mysql.connector
from mySQL import MySQLPassword
from flask import jsonify

dbconfig={
    "host":"localhost",
    "port":"3306",
    "database":"mydatabase",
    "user":"root",
    "password":MySQLPassword(),
}
cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 10,
                                                      pool_reset_session = True,
                                                      **dbconfig)

def check_username(username):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="SELECT username FROM member WHERE username =%s"
        val=(username)
        mycursor.execute(sql, (val,))
        result=mycursor.fetchall()
        return result
    except:
        print("Unexpected Error from check_username()")
    finally:
        mycursor.close()
        cnx.close()

def insert_signupinfo(new_name, username_check, new_pwd):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val=(new_name, username_check, new_pwd)
        mycursor.execute(sql, val)
        cnx.commit()
    except:
        print("Unexpected Error from insert_signupinfo()")
    finally:
        mycursor.close()
        cnx.close()

def check_signin(username):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="SELECT * FROM member WHERE username =%s"
        val=(username)
        mycursor.execute(sql, (val,))
        result=mycursor.fetchone()
        return result
    except:
        print("Unexpected Error from check_signin()")
    finally:
        mycursor.close()
        cnx.close()   

def create_msg(member_id, content):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="INSERT INTO message (member_id, content) VALUES (%s, %s)"
        val=(member_id, content)
        mycursor.execute(sql, val)
        cnx.commit()
    except:
        print("Unexpected Error from create_msg()")
    finally:
        mycursor.close()
        cnx.close()

def get_msgs():
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY time DESC"
        mycursor.execute(sql)
        msgs=mycursor.fetchall()
        return msgs
    except:
        print("Unexpected Error from get_msgs()")
    finally:
        mycursor.close()
        cnx.close()

def getmemberinfo(username_input):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql="SELECT * FROM member WHERE username =%s"
        val=(username_input)
        mycursor.execute(sql, (val,))
        result=mycursor.fetchone()
        if result==None:
            memberinfo=None
            return jsonify({"data":memberinfo})
        else:
            if result is not None:
                memberinfo={
                    "id":result[0],
                    "name":result[1],
                    "username":result[2]
                }
                return jsonify({"data":memberinfo})
    except:
        print("Unexpected Error from getmemberinfo()")
    finally:
        mycursor.close()
        cnx.close()

def rename(name_input, name_insession):
    try:
        cnx=cnxpool.get_connection()
        mycursor=cnx.cursor()
        sql_set="set sql_safe_updates=0"
        sql_update="update member set name=%s where name =%s"
        sql_result="SELECT * FROM member WHERE name =%s"
        val_update=(name_input, name_insession)
        val_result=(name_input)
        mycursor.execute(sql_set)
        mycursor.execute(sql_update, val_update)
        cnx.commit()
        mycursor.execute(sql_result, (val_result,))
        result=mycursor.fetchone()
        if result==None:
            error_response=True
            return jsonify({"error":error_response})
        else:
            if result is not None:
                success_response=True
                return jsonify({"ok":success_response})
    except:
        print("Unexpected Error from rename()")
    finally:
        mycursor.close()
        cnx.close()


# mydb=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password=MySQLPassword(),
#         database="mydatabase"
#     )