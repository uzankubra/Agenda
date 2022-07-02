from tkinter import *
import sqlite3
from tkinter import messagebox


def gunYaz():
    global gun
    gun=deger1.get()
    

def ayYaz():
    global ay
    ay=deger2.get()

def yilYaz():
    global yil
    yil=deger3.get()
    
def ekle():
    global metin
    global gun
    global ay
    global yil
    global tarih
    gunYaz()
    ayYaz()
    yilYaz()
    metin= metinKutusu.get(1.0, END)
    metinKutusu.delete(1.0, END)
    tarih=gun +" "+ay+" "+yil

    try:
        im.execute(''' INSERT INTO ajanda(Tarih,Notlar) VALUES (?,?)''', (tarih,metin))
        messagebox.showinfo("Bilgi", "Kayıt başarıyla girildi.")

    except:
        messagebox.showerror("Hata","Belirtilen tarihte zaten bir kayıt var." )
    baglanti.commit()

def getir():
    global gun
    global ay
    global yil
    gunYaz()
    ayYaz()
    yilYaz()
    tarih= gun+" "+ay+" "+yil
    im.execute("SELECT Notlar FROM ajanda WHERE Tarih= ? ", (tarih,))
    veri = im.fetchall()
    metinKutusu.insert(1.0,veri)



tarih=""
baglanti=sqlite3.connect('Ajanda.db')
im=baglanti.cursor()
im.execute("CREATE TABLE IF NOT EXISTS ajanda (Tarih TEXT UNIQUE, Notlar TEXT)")

pencere=Tk()

pencere.geometry("600x400")

pencere.title("Notlar")

cerceve=Frame()

cerceve.pack(side=BOTTOM, fill=X)

deger1=StringVar()
deger2=StringVar()
deger3=StringVar()

aylar= "Ocak", "Şubat", "Mart", "Nisan", "Mayıs","Haziran", "Temmuz", "Ağustos","Eylül", "Ekim","Kasım", "Aralık"
                 
secim_Gun=Spinbox(pencere,from_=1, to=31, width=5, command=gunYaz, textvariable= deger1)

secim_Ay=Spinbox(pencere, values=aylar,width=12, command=ayYaz, textvariable=deger2)

secim_yil=Spinbox(pencere, font=12, from_=2020, to=2023, width=5, command=yilYaz, textvariable=deger3)

secim_Gun.pack(side=LEFT)
secim_Ay.pack(side=LEFT)
secim_yil.pack(side=LEFT)


dugmeCikis=Button(pencere, text="Çıkış", command=pencere.destroy)

dugmeEkle=Button(pencere, text="Ekle", command=ekle)

dugmeGetir=Button(pencere, text="Getir", command=getir)


dugmeCikis.pack(side= RIGHT, padx=20)
dugmeGetir.pack(side= RIGHT, padx=20)
dugmeEkle.pack(side= RIGHT, padx=20)



dikeySb=Scrollbar(cerceve, orient=VERTICAL)

dikeySb.pack(side=RIGHT, fill=Y)

metinKutusu=Text(cerceve, width=600, height=15, wrap= WORD, yscrollcommand=dikeySb.set)


metinKutusu.pack()
                 
dikeySb.config(command=metinKutusu.yview)

pencere.mainloop()






                 
