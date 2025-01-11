import sqlite3

def create_tables():
    conn = sqlite3.connect('veresiye_takip.db')
    cursor = conn.cursor()

    # Müşteri ve borç tablolarını oluşturur
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Musteri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        telefon TEXT,
        adres TEXT,
        notlar TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Borc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        musteri_id INTEGER,
        tarih TEXT,
        tutar REAL,
        aciklama TEXT,
        FOREIGN KEY (musteri_id) REFERENCES Musteri (id)
    )
    ''')
    conn.commit()
    conn.close()