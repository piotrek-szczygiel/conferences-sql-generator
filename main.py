import pyodbc

from db import DB

if __name__ == '__main__':
    conf_count = int(input('enter number of conferences to generate: '))

    print('generating database...')
    db = DB(conf_count)
    db.generate()
    result = db.to_sql()

    result_file = 'result.sql'
    conn_file = 'conn.txt'

    print('writing result into {}...'.format(result_file))
    with open(result_file, 'wb') as file:
        file.write(result.encode('utf-8'))

    print('reading connection settings from {}...'.format(conn_file))
    with open(conn_file, 'r') as file:
        conn_settings = file.read()

        print('connecting to database...')
        with pyodbc.connect(conn_settings) as conn:
            print('inserting data for {} conferences...'.format(conf_count))
            cursor = conn.cursor()
            cursor.execute(result)
            conn.commit()

            print('data successfully inserted')
            print('sql result contains {} lines'.format(result.count('\n')))
