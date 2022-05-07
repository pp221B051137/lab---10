import psycopg2
from config2 import config2

def update_user(user_id, username):
    sql = """
    update accounts
    set username = %s
    where user_id = %s;
    """
    conn = None
    updated_rows = 0
    try:
        params = config2()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
s = str(input())
update_user(1, s)