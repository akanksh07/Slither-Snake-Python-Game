import sqlite3
import datetime,time

def connect():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS 
                leaderboard ( 
                score integer, 
                name text,
                timestamp date)''')
    conn.commit()
    conn.close()

def insert_record(score,name,timestamp):
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO leaderboard VALUES (?,?,?)",(score,name,timestamp))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM leaderboard")
    rows=cur.fetchall()
    conn.close()
    return rows

def bottom_record():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM leaderboard  ORDER BY score ASC")
    rows=cur.fetchall()
    conn.close()
    return rows[0][0]

def snakes_highscore():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM leaderboard  ORDER BY score DESC")
    rows=cur.fetchall()
    conn.close()
    return rows[0][0]

def display_leaderboard():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM leaderboard  ORDER BY score DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def reset_leaderboard():
    conn=sqlite3.connect("leaderboard_data.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE leaderboard ")
    conn.close()
    connect()
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
    insert_record(0, "----", "---")
 
connect()
# insert_record(0, 'Developer1',datetime.datetime.now() )
# insert_record(-1, 'Developer2',datetime.datetime.now() )
# insert_record(-2, 'Developer3',datetime.datetime.now() )
# insert_record(-6, 'Developer4',datetime.datetime.now() )
# insert_record(2, 'Developer5',datetime.datetime.now() )
# insert_record(4, 'Developer6',datetime.datetime.now() )
# insert_record(7, 'Developer5',datetime.datetime.now() )
# insert_record(8, 'Developer6',datetime.datetime.now() )
# insert_record(22, 'Developer5',datetime.datetime.now() )

#reset_leaderboard()
print(view())
print(bottom_record())