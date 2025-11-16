"""
agent_memory.py
Handles session and memory management using SQLite.
Simulates persistent user sessions and stores user-agent interactions.
"""

import sqlite3

# Connect to an in-memory database (or file DB for persistence)
conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create tables for resource data and user session history
c.execute('''
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    latitude REAL,
    longitude REAL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS sessions (
    user_id TEXT NOT NULL,
    session_id TEXT NOT NULL,
    request TEXT,
    response TEXT
)
''')

conn.commit()

def save_resource(id, name, r_type, lat, lng):
    """Insert or update a resource entry in the database."""
    c.execute('''
    INSERT OR REPLACE INTO resources (id, name, type, latitude, longitude)
    VALUES (?, ?, ?, ?, ?)''', (id, name, r_type, lat, lng))
    conn.commit()

def get_resources_by_type(r_type):
    """Fetch all resources of a specific type."""
    c.execute('SELECT name, latitude, longitude FROM resources WHERE type=?', (r_type,))
    return c.fetchall()
