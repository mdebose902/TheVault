from xml.dom import UserDataHandler
import psycopg2
from config import config
from hash import hasher


def insert():

    #data to be inserted

    #SQL query to insert data
    SQL = "INSERT INTO accounts (site,username,password) VALUES (%s,%s,%s)"

    #getting user input
    website = input("Website: ")
    username = input("Username: ")
    password = input("password: ")

    #data tuple
    data = (website,username,hasher(password))
    website = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(SQL,data)
        conn.commit()
        website = cur.fetchall()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return website


if __name__== "__main__":
    insert()
