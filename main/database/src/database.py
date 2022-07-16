import json

import psycopg2.extras


def getCredentials(target, filename):
    with open(filename) as f:
        data = json.load(f)
        credential = data[target]
        return credential


def insertValues(msg):
    insert_values = []
    id = ''
    name = ''
    discord_num = ''
    discord_id = ''
    quote = ''
    cur.execute(insert_values)


conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=getCredentials('host', 'config.json'),
        dbname=getCredentials('dbname', 'config.json'),
        user=getCredentials('user', 'config.json'),
        password=getCredentials('password', 'config.json'),
        port=getCredentials('port', 'config.json'))

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DROP TABLE IF EXISTS quotes')

    create_script = ''' CREATE TABLE IF NOT EXISTS quotes (
                            id int PRIMARY KEY,
                            name varchar(40),
                            discord_num int,
                            discord_id varchar(50),
                            quote varchar(500))'''

    cur.execute(create_script)
    insert_script = 'INSERT INTO quotes (id, name, discord_num, discord_id, quote) VALUES(%s,%s,%s,%s)'

    cur.execute('SELECT * FROM quote')

    for user_quote in cur.fetchall():
        print(user_quote['quote'])

    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
