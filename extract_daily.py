import sqlite3
from time import time


DATABASE_FILE = 'weewx.sdb'

SECS_IN_A_DAY = 24*60*60


def generate_sql():
    sql = ('select * from archive '
          'where dateTime between {} and {};')

    time_ = int(time())
    return sql.format(time_ - SECS_IN_A_DAY, time_)


def main():
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()
        cur.execute(generate_sql())
        data = cur.fetchall()
        for line in data:
            print(line)


if __name__ == '__main__':
    main()
