import tkinter as tk
from tkinter import ttk
from fonksiyon import (
    musteri_ekle,
    musteri_guncelle,
    musteri_sil,
    borclari_listele,
    borc_ekle,
    combobox_guncelle,
)

def create_widgets(frame_musteri, frame_borc, frame_borc_ekle):
    # Müşteri Yönetimi Sekmesi
    frame1 = ttk.LabelFrame(frame_musteri, text="Müşteri Bilgileri", padding="10")
    frame1.grid(row=0, column=0, sticky=(tk.W, tk.E))

    ad_label = ttk.Label(frame1, text="Ad:")
    ad_label.grid(row=0, column=0, padx=5, pady=5)
    ad_entry = ttk.Entry(frame1, width=30)
    ad_entry.grid(row=0, column=1, padx=5, pady=5)

    soyad_label = ttk.Label(frame1, text="Soyad:")
    soyad_label.grid(row=1, column=0, padx=5, pady=5)
    soyad_entry = ttk.Entry(frame1, width=30)
    soyad_entry.grid(row=1, column=1, padx=5, pady=5)

    telefon_label = ttk.Label(frame1, text="Telefon:")
    telefon_label.grid(row=2, column=0, padx=5, pady=5)
    telefon_entry = ttk.Entry(frame1, width=30)
    telefon_entry.grid(row=2, column=1, padx=5, pady=5)

    adres_label = ttk.Label(frame1, text="Adres:")
    adres_label.grid(row=3, column=0, padx=5, pady=5)
    adres_entry = ttk.Entry(frame1, width=30)
    adres_entry.grid(row=3, column=1, padx=5, pady=5)

    notlar_label = ttk.Label(frame1, text="Notlar:")
    notlar_label.grid(row=4, column=0, padx=5, pady=5)
    notlar_text = tk.Text(frame1, width=30, height=5)
    notlar_text.grid(row=4, column=1, padx=5, pady=5)

    ekle_button = ttk.Button(frame1, text="Ekle", command=lambda: musteri_ekle(ad_entry, soyad_entry, telefon_entry, adres_entry, notlar_text, musteri_tree, combobox_guncelle))
    ekle_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    guncelle_button = ttk.Button(frame1, text="Güncelle", command=lambda: musteri_guncelle(ad_entry, soyad_entry, telefon_entry, adres_entry, notlar_text, musteri_tree, combobox_guncelle))
    guncelle_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

    sil_button = ttk.Button(frame1, text="Sil", command=lambda: musteri_sil(musteri_tree, combobox_guncelle))
    sil_button.grid(row=6, column=0, columnspan=2, pady=10)

    columns = ('id', 'ad', 'soyad', 'telefon', 'adres', 'notlar')
    musteri_tree = ttk.Treeview(frame_musteri, columns=columns, show='headings')
    for col in columns:
        musteri_tree.heading(col, text=col)
    musteri_tree.grid(row=1, column=0, padx=10, pady=10)

    # Borç Yönetimi Sekmesi
    frame2 = ttk.LabelFrame(frame_borc, text="Borç Yönetimi", padding="10")
    frame2.grid(row=0, column=0, sticky=(tk.W, tk.E))

    borc_listeleme_combobox_label = ttk.Label(frame2, text="Müşteri Adı:")
    borc_listeleme_combobox_label.grid(row=0, column=0, padx=5, pady=5)
    borc_listeleme_combobox = ttk.Combobox(frame2, width=30)
    borc_listeleme_combobox.grid(row=0, column=1, padx=5, pady=5)

    borc_listele_button = ttk.Button(frame2, text="Borçları Listele", command=lambda: borclari_listele(borc_tree, borc_listeleme_combobox.get()))
    borc_listele_button.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

    borc_columns = ('id', 'musteri_id', 'tarih', 'tutar', 'aciklama')
    borc_tree = ttk.Treeview(frame2, columns=borc_columns, show='headings')
    for col in borc_columns:
        borc_tree.heading(col, text=col)
    borc_tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Borç Ekleme Sekmesi
    frame3 = ttk.LabelFrame(frame_borc_ekle, text="Borç Ekleme", padding="10")
    frame3.grid(row=0, column=0, sticky=(tk.W, tk.E))

    borc_musteri_combobox_label = ttk.Label(frame3, text="Müşteri Adı:")
    borc_musteri_combobox_label.grid(row=0, column=0, padx=5, pady=5)
    borc_musteri_combobox = ttk.Combobox(frame3, width=30)
    borc_musteri_combobox.grid(row=0, column=1, padx=5, pady=5)

    borc_tarih_label = ttk.Label(frame3, text="Tarih:")
    borc_tarih_label.grid(row=1, column=0, padx=5, pady=5)
    borc_tarih_entry = ttk.Entry(frame3, width=30)
    borc_tarih_entry.grid(row=1, column=1, padx=5, pady=5)

    borc_tutar_label = ttk.Label(frame3, text="Tutar:")
    borc_tutar_label.grid(row=2, column=0, padx=5, pady=5)
    borc_tutar_entry = ttk.Entry(frame3, width=30)
    borc_tutar_entry.grid(row=2, column=1, padx=5, pady=5)

    borc_aciklama_label = ttk.Label(frame3, text="Açıklama:")
    borc_aciklama_label.grid(row=3, column=0, padx=5, pady=5)
    borc_aciklama_text = tk.Text(frame3, width=30, height=5)
    borc_aciklama_text.grid(row=3, column=1, padx=5, pady=5)

    borc_ekle_button = ttk.Button(frame3, text="Borç Ekle", command=lambda: borc_ekle(borc_musteri_combobox, borc_tarih_entry, borc_tutar_entry, borc_aciklama_text, borc_tree))
    borc_ekle_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)