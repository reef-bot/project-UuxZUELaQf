import sqlite3

def log_user_activity(user, activity):
    # Connect to SQLite database
    conn = sqlite3.connect('../database/moderation_logs.db')
    c = conn.cursor()
    # Insert the user activity log
    c.execute('INSERT INTO user_activity (user, activity) VALUES (?, ?)', (user, activity))
    conn.commit()
    conn.close()