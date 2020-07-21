import socket
import time
from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDTimePicker, MDThemePicker, MDDatePicker
import sqlite3


class studyology(MDApp):
    Config.set('graphics', 'resizable', True)

    def build(self):
        self.icon = 'bg\\logo.png'
        return Builder.load_file('master.kv')

    def on_start(self):
        try:
            conn = sqlite3.connect("data4app.db")
            a = conn.cursor()
            b = conn.cursor()
            c = conn.cursor()
            a.execute('SELECT * FROM MyAcc')
            b.execute('SELECT * FROM MyAcc')
            c.execute('SELECT * FROM MyAcc')
            myname = a.fetchone()[0]
            mynum = b.fetchone()[1]
            mymail = c.fetchone()[2]
            self.root.ids.screen_manager.current = 'cl'
        except:
            pass

    def otp(self):
        if self.root.ids.otp.text != '':
            self.dialog = MDDialog(
                size=('150dp', '150dp'),
                size_hint=(None, None),
                text="INCORRECT OTP",
            )
            self.dialog.open()

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def get_time(self, instance, time):
        print(time)
        self.root.ids.time.text = str(time)

    def regis(self):
        soc = socket.socket()
        server_host = '192.168.137.1'
        port = 1024
        soc.connect((server_host, port))
        soc.send('regis'.encode())
        time.sleep(.2)

        e = self.root.ids.e_m.text
        naam = self.root.ids.naam.text
        nuum = self.root.ids.nuum.text
        soc.send(nuum.encode())
        time.sleep(.2)
        print("send number")
        soc.send(e.encode())
        time.sleep(.2)
        print("send email")
        soc.send(naam.encode())
        print("send name")
        num = (soc.recv(1024))
        num = num.decode()
        e = (soc.recv(1024))
        e = e.decode()
        nam = (soc.recv(1024))
        nam = nam.decode()

        soc.close()

    def get_date(self, date):
        self.root.ids.date.text = str(date)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def login(self):

        soc = socket.socket()
        server_host = '192.168.137.1'
        number = self.root.ids.number.text
        port = 1024
        soc.connect((server_host, port))
        soc.send('login'.encode())
        time.sleep(.2)
        soc.send(number.encode())
        num = (soc.recv(1024))
        num = num.decode()
        e = (soc.recv(1024))
        e = e.decode()
        nam = (soc.recv(1024))
        nam = nam.decode()
        self.root.ids.cont.nam = nam
        print(nam)
        self.root.ids.cont.em = e
        print(e)
        self.root.ids.cont.num = num
        print(num)
        soc.close()

    def som_warn(self):
        if self.root.ids.screen_manager.current == 'login':
            self.connect = MDDialog(
                size=('150dp', '150dp'),
                size_hint=(None, None),
                text="something is incorrect",
            )
            self.connect.open()

    def delay(self):
        time.sleep(1)

    def logtodata(self):
        conn = sqlite3.connect("data4app.db")
        a = conn.cursor()
        a.execute(f'INSERT INTO MyAcc VALUES(?,?,?)',
                  (self.root.ids.name.text, self.root.ids.number.text, self.root.ids.em.text))
        conn.commit()
        conn.close()

    def test_info(self):
        z = socket.socket()
        server_host = '192.168.137.1'
        port = 1024
        z.connect((server_host, port))
        z.send('refresh'.encode())
        math_t = (z.recv(1024))
        math_d = (z.recv(1024))
        math_des = (z.recv(1024))

        bio_t = (z.recv(1024))
        bio_d = (z.recv(1024))
        bio_des = (z.recv(1024))

        phy_t = (z.recv(1024))
        phy_d = (z.recv(1024))
        phy_des = (z.recv(1024))

        chem_t = (z.recv(1024))
        chem_d = (z.recv(1024))
        chem_des = (z.recv(1024))

        hist_t = (z.recv(1024))
        hist_d = (z.recv(1024))
        hist_des = (z.recv(1024))

        civ_t = (z.recv(1024))
        civ_d = (z.recv(1024))
        civ_des = (z.recv(1024))

        pbi_t = (z.recv(1024))
        pbi_d = (z.recv(1024))
        pbi_des = (z.recv(1024))

        hin_t = (z.recv(1024))
        hin_d = (z.recv(1024))
        hin_des = (z.recv(1024))

        geo_t = (z.recv(1024))
        geo_d = (z.recv(1024))
        geo_des = (z.recv(1024))

        z.close()
        math = self.root.ids.math
        math.secondary_text = math_des
        math.tertiary_text = f'on {math_d},time: {math_t}'

        bio = self.root.ids.bio
        bio.secondary_text = bio_des
        bio.tertiary_text = f'on {bio_d},time: {bio_t}'

        chem = self.root.ids.chem
        chem.secondary_text = chem_des
        chem.tertiary_text = f'on {chem_d},time: {chem_t}'

        phy = self.root.ids.phy
        phy.secondary_text = phy_des
        phy.tertiary_text = f'on {phy_d},time: {phy_t}'

        hist = self.root.ids.hist
        hist.secondary_text = hist_des
        hist.tertiary_text = f'on {hist_d},time: {hist_t}'

        civ = self.root.ids.civ
        civ.secondary_text = civ_des
        civ.tertiary_text = f'on {civ_d},time: {civ_t}'

        pbi = self.root.ids.pbi
        pbi.secondary_text = pbi_des
        pbi.tertiary_text = f'on {pbi_d},time: {pbi_t}'

        hin = self.root.ids.hin
        hin.secondary_text = hin_des
        hin.tertiary_text = f'on {hin_d},time: {hin_t}'

        geo = self.root.ids.geo
        geo.secondary_text = geo_des
        geo.tertiary_text = f'on {geo_d},time: {geo_t}'


# TODO: ADD CHEM AND PHY AS WELL AS ADD PBI HINDI ETC. AT CL SCREEN,
#  self.root.ids.screen_manager.current = 'otp',{self.root.ids.name.text},{self.root.ids.number.text},
#  {self.root.ids.em.text}

if __name__ == '__main__':
    studyology().run()
