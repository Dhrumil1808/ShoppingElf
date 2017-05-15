
from Models import UserPojo
import mysql.connector
import DbConstants
import collections

def addUser(user):
    print "adding user"
    message = "SUCCESS"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """insert into user (username,password, family_members) VALUES (%s,%s,%s)"""
        cursor.execute(query, (user.email,user.password, user.family_members))
    except mysql.connector.Error as err:
            message ="FAILURE"
            print "Something went wrong: {}" + format(err)



    database.commit()
    cursor.close()
    database.close()
    d = collections.OrderedDict()
    d['message'] = message;
    return d



def updateUserPassword(user):
    print "adding user"
    message = "SUCCESS"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """update  user set password=%s where username =%s"""
        cursor.execute(query, (user.password,user.email))
    except mysql.connector.Error as err:
        message = "FAILURE"
        print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    d = collections.OrderedDict()
    d['message'] = message;
    return d


def updateFamilyMembers(user):
    print "adding user"
    message = "SUCCESS"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """update  user set family_members=%s where username =%s"""
        cursor.execute(query, (user.family_members,user.email))
    except mysql.connector.Error as err:
        message = "FAILURE"
        print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    d = collections.OrderedDict()
    d['message'] = message;
    return d



def updateApiKey(email,api_key):
    print "updating user"
    message = "SUCCESS"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """update  user set user_api_key=%s where username =%s"""
        cursor.execute(query, (api_key,email))
    except mysql.connector.Error as err:
        message = "FAILURE"
        print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    d = collections.OrderedDict()
    d['message'] = message;
    return d



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
        authenticated= "ACCESS_DENIED"


    cursor.close()
    database.close()
    d = collections.OrderedDict()
    d['message'] = authenticated;
    return d

    return d;