
from Models import UserPojo
import mysql.connector
import DbConstants

def addUser(user):
    print "adding user"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """insert into user (username,password, family_members) VALUES (%s,%s,%s)"""
        cursor.execute(query, (user.email,user.password, user.family_members))
    except mysql.connector.Error as err:
            print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    return "successful insert"



def updateUserPassword(user):
    print "adding user"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """update  user set password=%s where username =%s"""
        cursor.execute(query, (user.password,user.email))
    except mysql.connector.Error as err:
            print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    return "successful update"


def updateFamilyMembers(user):
    print "adding user"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """update  user set family_members=%s where username =%s"""
        cursor.execute(query, (user.family_members,user.email))
    except mysql.connector.Error as err:
            print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    return "successful update"


def findUser(username,password):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    userid = None
    authenticated= "ACCESS_DENIED";

    try:
        query = """SELECT userid FROM user where username= %s and password=%s"""
        cursor.execute(query,(username,password))
        rows = cursor.fetchall()
        for user_row in rows:
            userid = user_row[0]
            break;
        print userid
        if userid is not None:
            authenticated = "ACCESS_GRANTED";
    except mysql.connector.Error as err:
        print "Something went wrong: {}" + format(err)
        cursor.close()
        database.close()
        return "ACCESS_DENIED"



    cursor.close()
    database.close()

    return authenticated;