from db import db
from sqlalchemy.sql import text
from flask import session
from chains import showchains

def deletechain(chain_id):
    sql = """DELETE FROM chains WHERE chain_id = :chain_id"""
    db.session.execute(text(sql), {'chain_id': chain_id})
    db.session.commit() 

def showchains():
    sql = "SELECT id, chain_name, area_id FROM chains"
    result = db.session.execute(text(sql))
    return result.fetchall()