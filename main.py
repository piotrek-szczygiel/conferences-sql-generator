import pyodbc
import time

from db import DB

if __name__ == '__main__':
    conf_count = int(input('enter number of conferences to generate: '))

    print('generating database for {} conferences'.format(conf_count))

    time1 = time.time()
    db = DB(conf_count)
    result = db.to_sql()
    time2 = time.time()

    print('generated database in {:.3f} s'.format(time2 - time1))

    result_file = 'result.sql'
    conn_file = 'conn.txt'

    print('writing {} lines into {}'.format(result.count('\n'), result_file))
    with open(result_file, 'wb') as file:
        file.write(result.encode('utf-8'))

    print('reading connection settings from {}'.format(conn_file))
    with open(conn_file, 'r') as file:
        conn_settings = file.read()

        print('connecting to database')
        with pyodbc.connect(conn_settings) as conn:
            print('inserting data into the database')

            time1 = time.time()
            cursor = conn.cursor()
            cursor.execute(result)
            conn.commit()
            time2 = time.time()

            print('inserted data in {:.3f} s'.format(time2 - time1))
