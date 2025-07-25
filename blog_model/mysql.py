import pymysql

MYSQL_HOST = "127.0.0.1"

MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user="jwpark114",
    passwd="nkf6435",
    db="blog_db",
    charset="utf8",
)


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
