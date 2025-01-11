import tkinter as tk
from tkinter import messagebox
import sqlite3

# Veritabanı bağlantısını oluşturur
conn = sqlite3.connect('veresiye_takip.db')
cursor = conn.cursor()

def musteri_ekle(ad_entry, soyad_entry, telefon_entry, adres_entry, notlar_text, musteri_tree, combobox_guncelle):
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    telefon = telefon_entry.get()
    adres = adres_entry.get()
    notlar = notlar_text.get("1.0", tk.END).strip()
    if ad and soyad:
        cursor.execute('''
        INSERT INTO Musteri (ad, soyad, telefon, adres, notlar)
        VALUES (?, ?, ?, ?, ?)
        ''', (ad, soyad, telefon, adres, notlar))
        conn.commit()
        messagebox.showinfo("Başarılı", "Müşteri eklendi.")
        musterileri_listele(musteri_tree)
        combobox_guncelle()
    else:
        messagebox.showwarning("Hata", "Ad ve soyad alanları boş bırakılamaz.")

def musteri_guncelle(ad_entry, soyad_entry, telefon_entry, adres_entry, notlar_text, musteri_tree, combobox_guncelle):
    selected_item = musteri_tree.selection()[0]
    selected_id = musteri_tree.item(selected_item)['values'][0]
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    telefon = telefon_entry.get()
    adres = adres_entry.get()
    notlar = notlar_text.get("1.0", tk.END).strip()
    if ad and soyad:
        cursor.execute('''
        UPDATE Musteri
        SET ad = ?, soyad = ?, telefon = ?, adres = ?, notlar = ?
        WHERE id = ?
        ''', (ad, soyad, telefon, adres, notlar, selected_id))
        conn.commit()
        messagebox.showinfo("Başarılı", "Müşteri güncellendi.")
        musterileri_listele(musteri_tree)
        combobox_guncelle()
    else:
        messagebox.showwarning("Hata", "Ad ve soyad alanları boş bırakılamaz.")

def musteri_sil(musteri_tree, combobox_guncelle):
    selected_item = musteri_tree.selection()[0]
    selected_id = musteri_tree.item(selected_item)['values'][0]
    cursor.execute('''
    DELETE FROM Musteri WHERE id = ?
    ''', (selected_id,))
    conn.commit()
    messagebox.showinfo("Başarılı", "Müşteri silindi.")
    musterileri_listele(musteri_tree)
    combobox_guncelle()

def musterileri_listele(musteri_tree):
    for row in musteri_tree.get_children():
        musteri_tree.delete(row)
    cursor.execute('SELECT * FROM Musteri')
    for row in cursor.fetchall():
        musteri_tree.insert('', 'end', values=row)

def borc_ekle(borc_musteri_combobox, borc_tarih_entry, borc_tutar_entry, borc_aciklama_text, borc_tree):
    musteri_ad = borc_musteri_combobox.get()
    cursor.execute('SELECT id FROM Musteri WHERE ad = ?', (musteri_ad,))
    musteri_id = cursor.fetchone()
    if musteri_id:
        musteri_id = musteri_id[0]
        tarih = borc_tarih_entry.get()
        tutar = borc_tutar_entry.get()
        aciklama = borc_aciklama_text.get("1.0", tk.END).strip()
        if tarih and tutar:
            cursor.execute('''
            INSERT INTO Borc (musteri_id, tarih, tutar, aciklama)
            VALUES (?, ?, ?, ?)
            ''', (musteri_id, tarih, tutar, aciklama))
            conn.commit()
            messagebox.showinfo("Başarılı", "Borç eklendi.")
            borclari_listele(borc_tree, musteri_ad)
        else:
            messagebox.showwarning("Hata", "Tarih ve tutar alanları boş bırakılamaz.")
    else:
        messagebox.showwarning("Hata", "Geçersiz müşteri seçimi.")

def borclari_listele(borc_tree, musteri_ad):
    for row in borc_tree.get_children():
        borc_tree.delete(row)
    cursor.execute('SELECT id FROM Musteri WHERE ad = ?', (musteri_ad,))
    musteri_id = cursor.fetchone()
    if musteri_id:
        musteri_id = musteri_id[0]
        cursor.execute('SELECT * FROM Borc WHERE musteri_id = ?', (musteri_id,))
        for row in cursor.fetchall():
            borc_tree.insert('', 'end', values=row)
    else:
        messagebox.showwarning("Hata", "Geçersiz müşteri seçimi.")

def combobox_guncelle(borc_musteri_combobox, borc_listeleme_combobox):
    cursor.execute('SELECT ad FROM Musteri')
    musteriler = cursor.fetchall()
    borc_musteri_combobox['values'] = [musteri[0] for musteri in musteriler]
    borc_listeleme_combobox['values'] = [musteri[0] for musteri in musteriler]
    borc_musteri_combobox.set('')
    borc_listeleme_combobox.set('')