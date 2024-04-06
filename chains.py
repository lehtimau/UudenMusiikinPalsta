from db import db
from sqlalchemy.sql import text
from flask import session


#List the chains

def showchains(area_id):
    sql = "SELECT id, chain_name, area_id FROM chains WHERE area_id=:areaid"
    result = db.session.execute(text(sql), {'areaid': area_id})
    return result.fetchall()

#Function to add chains

def add_chain(title, area_id):
    sql = """INSERT INTO chains (chain_name, area_id)
        VALUES (:title, :area_id)"""
    db.session.execute(text(sql), {'title': title, 'area_id': area_id})
    db.session.commit()

#Function to get chain ID

def get_id():
    sql = """SELECT id FROM chains ORDER BY
    id DESC LIMIT 1"""
    result = db.session.execute(text(sql))
    return result.fetchone()[0]