import sqlite3

def log_moderation_action(action, moderator, user, reason):
    # Connect to SQLite database
    conn = sqlite3.connect('../database/moderation_logs.db')
    c = conn.cursor()
    # Insert the log entry
    c.execute('INSERT INTO moderation_logs (action, moderator, user, reason) VALUES (?, ?, ?, ?)', (action, moderator, user, reason))
    conn.commit()
    conn.close()