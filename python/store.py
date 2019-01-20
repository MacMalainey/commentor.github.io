import sqlite3
import threading
from github import RateLimitExceededException, GithubException
from time import time, sleep
conn = None
cursor = None
database_lock = None


def setup():
    global conn, cursor, database_lock
    database_lock = threading.Lock()
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

def add_data(page, repo, code, comments, gcontext):
    global cursor, database_lock
    try:
        stars = repo.stargazers_count
        contrib = len(repo.get_contributors().totalCount)
    except RateLimitExceededException:
        seconds_till_reset = gcontext.rate_limiting_resettime - time()
        print("sleeping: " + str(seconds_till_reset))
        sleep(seconds_till_reset)
        stars = len(repo.get_stargazers())
        contrib = len(repo.get_stats_contributors())
    except GithubException:
        return
    database_lock.acquire()
    cursor.execute("INSERT (?, ?, ?, ?, ?) INTO tableau", page, comments, code, contrib, stars)
    cursor.commit()
    database_lock.release()

def close():
    cursor.close()
    conn.close()



