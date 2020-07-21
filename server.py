import socket
import sqlite3
import time
# 192.168.137.1
from database import USERS

s = socket.socket()
host = socket.gethostname()
print(host)
s.bind((host, 1024))
s.listen(99999999)
i = 0

condition = "true"

while condition == "true":

    try:
        z, addr = s.accept()
        i = i + 1
        print(i)
        data = z.recv(1024)
        data = data.decode()

        if data.startswith('login'):
            conn = sqlite3.connect("data.db")
            mob_id = z.recv(1024)
            mob_id = mob_id.decode()

            a = conn.cursor()
            b = conn.cursor()
            c = conn.cursor()

            a.execute(f'SELECT * FROM users WHERE number ={mob_id}')
            b.execute(f'SELECT * FROM users WHERE number ={mob_id}')
            c.execute(f'SELECT * FROM users WHERE number ={mob_id}')

            mob = str(a.fetchone()[0])
            z.send(mob.encode())
            time.sleep(1)

            elect_mail = b.fetchone()[1]
            z.send(elect_mail.encode())
            time.sleep(1)

            nam = c.fetchone()[2]
            z.send(nam.encode())
            conn.close()
            z.close()

        elif data.startswith('regis'):
            nu = z.recv(1024)  # var 1
            nu = nu.decode()
            email = z.recv(1024)  # var 2
            email = email.decode()
            na = z.recv(1024)  # var 3
            na = na.decode()
            new_user = USERS(nu, email, na)
            conn = sqlite3.connect("data.db")
            a = conn.cursor()
            a.execute('INSERT INTO users VALUES(?,?,?)', (new_user.number, new_user.e_mail, new_user.name))
            conn.commit()
            conn.close()
            z.send('done'.encode())
            z.close()

        elif data == 'test':
            sub = z.recv(1024)
            sub = sub.decode()
            des = z.recv(1024)
            des = des.decode()
            time = z.recv(1024)
            time = time.decode()
            date = z.recv(1024)
            date = date.decode()
            conn = sqlite3.connect('data2.db')
            cursor = conn.cursor()
            cursor.execute(f"UPDATE tests SET time = {time} where sub = {sub}")
            conn.commit()
            cursor.execute(f"UPDATE tests SET day = {date} where sub = {sub}")
            conn.commit()
            cursor.execute(f"UPDATE tests SET des = {des} where sub = {sub}")
            conn.commit()
            conn.close()

        elif data == 'refresh':

            conn = sqlite3.connect("data.db")

            math_t = conn.cursor()
            math_d = conn.cursor()
            math_des = conn.cursor()

            bio_t = conn.cursor()
            bio_d = conn.cursor()
            bio_des = conn.cursor()

            phy_t = conn.cursor()
            phy_d = conn.cursor()
            phy_des = conn.cursor()

            chem_t = conn.cursor()
            chem_d = conn.cursor()
            chem_des = conn.cursor()

            hist_t = conn.cursor()
            hist_d = conn.cursor()
            hist_des = conn.cursor()

            civ_t = conn.cursor()
            civ_d = conn.cursor()
            civ_des = conn.cursor()

            pbi_t = conn.cursor()
            pbi_d = conn.cursor()
            pbi_des = conn.cursor()

            hin_t = conn.cursor()
            hin_d = conn.cursor()
            hin_des = conn.cursor()

            geo_t = conn.cursor()
            geo_d = conn.cursor()
            geo_des = conn.cursor()

            math = "math"
            bio = "bio"
            phy = "phy"
            chem = 'chem'
            hist = 'hist'
            civ = 'civ'
            pbi = 'pbi'
            hin = 'hin'
            geo = 'geo'

            math_t.execute('SELECT * FROM tests WHERE sub = ?', (math,))
            math_d.execute('SELECT * FROM tests WHERE sub = ?', (math,))
            math_des.execute('SELECT * FROM tests WHERE sub = ?', (math,))

            bio_t.execute('SELECT * FROM tests WHERE sub = ?', (bio,))
            bio_d.execute('SELECT * FROM tests WHERE sub = ?', (bio,))
            bio_des.execute('SELECT * FROM tests WHERE sub = ?', (bio,))

            phy_t.execute('SELECT * FROM tests WHERE sub = ?', (phy,))
            phy_d.execute('SELECT * FROM tests WHERE sub = ?', (phy,))
            phy_des.execute('SELECT * FROM tests WHERE sub = ?', (phy,))

            chem_t.execute('SELECT * FROM tests WHERE sub = ?', (chem,))
            chem_d.execute('SELECT * FROM tests WHERE sub = ?', (chem,))
            chem_des.execute('SELECT * FROM tests WHERE sub = ?', (chem,))

            hist_t.execute('SELECT * FROM tests WHERE sub = ?', (hist,))
            hist_d.execute('SELECT * FROM tests WHERE sub = ?', (hist,))
            hist_des.execute('SELECT * FROM tests WHERE sub = ?', (hist,))

            civ_t.execute('SELECT * FROM tests WHERE sub = ?', (civ,))
            civ_d.execute('SELECT * FROM tests WHERE sub = ?', (civ,))
            civ_des.execute('SELECT * FROM tests WHERE sub = ?', (civ,))

            pbi_t.execute('SELECT * FROM tests WHERE sub = ?', (pbi,))
            pbi_d.execute('SELECT * FROM tests WHERE sub = ?', (pbi,))
            pbi_des.execute('SELECT * FROM tests WHERE sub = ?', (pbi,))

            hin_t.execute('SELECT * FROM tests WHERE sub = ?', (hin,))
            hin_d.execute('SELECT * FROM tests WHERE sub = ?', (hin,))
            hin_des.execute('SELECT * FROM tests WHERE sub = ?', (hin,))

            geo_t.execute('SELECT * FROM tests WHERE sub = ?', (geo,))
            geo_d.execute('SELECT * FROM tests WHERE sub = ?', (geo,))
            geo_des.execute('SELECT * FROM tests WHERE sub = ?', (geo,))

            z.send(math_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(math_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(math_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(bio_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(bio_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(bio_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(phy_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(phy_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(phy_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(chem_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(chem_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(chem_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(hist_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(hist_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(hist_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(civ_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(civ_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(civ_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(pbi_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(pbi_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(pbi_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(hin_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(hin_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(hin_des.fetchone()[3].encode())
            time.sleep(.2)

            z.send(geo_t.fetchone()[1].encode())
            time.sleep(.2)
            z.send(geo_d.fetchone()[2].encode())
            time.sleep(.2)
            z.send(geo_des.fetchone()[3].encode())
            z.close()
            conn.close()

    finally:
        pass
