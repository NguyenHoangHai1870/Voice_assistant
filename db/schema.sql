-- Users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Reminders / Calendar
CREATE TABLE IF NOT EXISTS reminders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    title TEXT,
    description TEXT,
    reminder_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- USER PROFILE
CREATE TABLE IF NOT EXISTS user_profiles (
    user_id INT PRIMARY KEY REFERENCES users(id),

    name TEXT,
    age INT,
    hometown TEXT,
    location TEXT,
    education TEXT,
    major TEXT,
    occupation TEXT,

    favorite_color TEXT,
    favorite_food TEXT,
    favorite_drink TEXT,

    relationship_status TEXT,
    birthday TEXT,
    company TEXT,

    prefers_short_answer BOOLEAN DEFAULT FALSE,
    prefers_detailed_answer BOOLEAN DEFAULT FALSE,
    prefers_formal_tone BOOLEAN DEFAULT FALSE,
    prefers_casual_tone BOOLEAN DEFAULT FALSE,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- HOBBIES
CREATE TABLE IF NOT EXISTS user_hobbies (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    hobby TEXT
);

-- CONVERSATION MEMORY
CREATE TABLE IF NOT EXISTS conversation_memory (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    role TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- USER BEHAVIORS
CREATE TABLE IF NOT EXISTS user_behaviors (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    action TEXT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);