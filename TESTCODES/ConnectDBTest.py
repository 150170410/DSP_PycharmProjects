import cx_Oracle


def db_connect():
    con = cx_Oracle.connect('DSP_MAIN/DSP_MAIN@localhost:8007/ENTELDSP')
    cur = con.cursor()
    cur.execute('select count(*) from tab');
    for row in cur:
        print (row)
    cur.close()
    con.close()
    print ('DB connection closed Successfully')


db_connect()
