from tkinter.tix import InputOnly
import psycopg2
from config2 import config2


def insert_account(username, phone):
    sql = """
    INSERT INTO accounts(username, phone)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config2()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username, phone))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id
n1 = str(input())
n2 = str(input())
insert_account(n1,n2)