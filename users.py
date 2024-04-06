from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import sys

def login(username, pword):
    sql = "SELECT id, pword FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {'username': username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.pword, pword):
            session["user_id"] = user.id
            return True
        else:
            return False
        

def register(username, pword):
    hash_value = generate_password_hash(pword)
    sql = "INSERT INTO users (username, pword, admin) VALUES (:username, :hash_value, 'f')"
    db.session.execute(text(sql), {"username": username, "hash_value": hash_value})
    db.session.commit()
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username": username})
    user_id = result.fetchone()[0]
    session["user_id"] = user_id

def logout():
    del session["user_id"]

def checkadmin(user_id):
    sql = "SELECT admin FROM users WHERE id=:user_id"
    result = db.session.execute(text(sql), {'user_id': user_id})
    admin = result.scalar()
    return admin 

    
def id():
    return session.get("user_id")