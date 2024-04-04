from flask import session
from db import db
from sqlalchemy.sql import text


def get_message_count(chain_id):
    sql = "SELECT COUNT(*) FROM messages WHERE chain_id = :chain_id"
    result = db.session.execute(text(sql), {"chain_id": chain_id})
    message_count = result.scalar()
    
    return message_count

def add_message(content, user_id, chain_id):
    sql = """INSERT INTO messages (content, user_id, chain_id) VALUES 
    (:content, :user_id, :chain_id)"""
    db.session.execute(text(sql), {'content': content, 'user_id': user_id, 'chain_id': chain_id})
    db.session.commit()

