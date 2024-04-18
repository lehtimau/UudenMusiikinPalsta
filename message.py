from flask import session
from db import db
from sqlalchemy.sql import text


#Function to get the message amount

def get_message_count(chain_id):
    sql = "SELECT COUNT(*) FROM messages WHERE chain_id = :chain_id"
    result = db.session.execute(text(sql), {"chain_id": chain_id})
    message_count = result.scalar()
    
    return message_count

#Add message

def add_message(content, user_id, chain_id):
    sql = """INSERT INTO messages (content, user_id, chain_id, sent_at) VALUES 
    (:content, :user_id, :chain_id, NOW())"""
    db.session.execute(text(sql), {'content': content, 'user_id': user_id, 'chain_id': chain_id})
    db.session.commit()

#Show messages

def showmessages(chain_id):
    sql = "SELECT messages.id, messages.content, messages.chain_id, messages.sent_at, users.username FROM messages, users WHERE chain_id=:chain_id AND users.id = messages.user_id ORDER BY messages.sent_at ASC"
    result = db.session.execute(text(sql), {'chain_id': chain_id})
    return result.fetchall()