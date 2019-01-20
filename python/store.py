import sqlite3
import threading
conn = None
cursor = None
database_lock = None


def setup():
    global conn, cursor, database_lock
    database_lock = threading.Lock()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

def addData(page, repo, code, comments):
    global cursor, database_lock
    stars = len(repo.get_stargazers())
    contrib = len(repo.get_stats_contributors())
    database_lock.acquire()
    cursor.execute("INSERT (?, ?, ?, ?, ?) INTO tableau", page, comments, code, contrib, stars)
    cursor.commit()
    database_lock.release()

def close():
    cursor.close()
    conn.close()



