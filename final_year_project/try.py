import sqlite3
con=sqlite3.connect('db.sqlite3')
work=()
for i in con.execute('SELECT name FROM sqlite_master WHERE type="table";'):
    print(i[0],con.execute(f'pragma table_info({i[0]})').fetchall())
    for j in con.execute(f'select * from {i[0]};').fetchall():print(j)
