CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    area_name TEXT,
    secrecy BOOLEAN,
    chain_amount INTEGER
);

CREATE TABLE chains (
    id SERIAL PRIMARY KEY,
    chain_name TEXT,
    message_amount INTEGER,
    area_id INTEGER REFERENCES areas
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    chain_id INTEGER REFERENCES chains,
    content TEXT,
    sent_at TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    pword TEXT, 
    admin BOOLEAN,
);

CREATE TABLE pro_users (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users
);