import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from fonksiyon import (
    musteri_ekle,
    musteri_guncelle,
    musteri_sil,
    borclari_listele,
    borc_ekle,
    combobox_guncelle,
)
from data import create_tables
from gorunum import create_widgets

# Veritabanı ve tablo oluşturma
create_tables()

# Tkinter ana penceresini oluşturur ve ttkbootstrap teması uygular
root = tb.Window(themename="superhero")
root.title("Veresiye Takip Uygulaması")
root.geometry("800x600")

# Notebook (sekme) oluşturur
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Sekmeleri oluştur
frame_musteri = ttk.Frame(notebook, padding="10")
notebook.add(frame_musteri, text='Müşteri Yönetimi')

frame_borc_ekle = ttk.Frame(notebook, padding="10")
notebook.add(frame_borc_ekle, text='Borç Ekleme Yönetimi')

frame_borc = ttk.Frame(notebook, padding="10")
notebook.add(frame_borc, text='Borç Yönetimi')

# Arayüz bileşenlerini oluştur
create_widgets(frame_musteri, frame_borc, frame_borc_ekle)

# Kombinasyon kutularını güncellemek için gerekli referansları al
borc_musteri_combobox = frame_borc_ekle.winfo_children()[0].winfo_children()[1]
borc_listeleme_combobox = frame_borc.winfo_children()[0].winfo_children()[1]

# Ana döngüyü başlatır
combobox_guncelle(borc_musteri_combobox, borc_listeleme_combobox)
root.mainloop()