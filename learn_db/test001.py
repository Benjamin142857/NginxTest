"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 3/2/2020
    Remark      : test001
"""
import pymysql


db_conn = pymysql.connect(
    "localhost",
    "root",
    "happy981206",
    "db_learn"
)
cur = db_conn.cursor()
sql = """
select * from score
"""
print(cur.execute(sql))

