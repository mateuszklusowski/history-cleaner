import sqlite3


def delete(site) -> str:

    with sqlite3.connect('YOUR GOOGLE PROFILE HISTORY FILE PATH') as conn:
        c = conn.cursor()

        while True:
            ids = []

            for row in c.execute(f'SELECT id, url FROM urls WHERE url LIKE "%{site}%"'):
                print(row)
                id = row[0]
                ids.append((id,))
            
            c.executemany('DELETE FROM urls WHERE id=?', ids)
            conn.commit()
            break
    

delete("YOUR SITE")
