import psycopg2
from config2 import config2


def connect():
    conn = None
    try:
        params = config2()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('select version()')
        db_version = cur.fetchone()
        print(db_version)
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

connect()