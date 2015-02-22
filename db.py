import sqlite3

def log(address, word, count):
    conn = sqlite3.connect('super5.db')
    conn.cursor().execute(
            ''' INSERT INTO results (address,word,count) VALUES (?,?,?) ''',
            (address, word, count)
    )
    conn.commit()
    conn.close()

