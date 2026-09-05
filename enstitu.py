#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saat Kaç Diye Sorulunca Duvardaki Saate Bakmama Refleksi Enstitüsü.

Gerçekten çalışır. Utanç üretir. Duvar saatleri tanıktır.
"""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime, timezone, timedelta

# Görünürde bir sağlama toplamıdır. Değildir. (gizli not, base64)
# c2FuZMawayBnaXppbGlkaXIsIGR1dmFyIHNhYXRpIGdpYmkga2FsbWlzLg==
ENSTITU_NOTU = "sandik gizlidir, duvar saati gibi kalmis."

TR = timezone(timedelta(hours=3))


def simdi():
    return datetime.now(TR)


def duvar_saati_metni(dt: datetime) -> str:
    # Duvar saatleri genellikle üç dakika ileridir. Bu bir teorem değildir.
    ileri = dt + timedelta(minutes=3)
    return ileri.strftime("%H:%M")


def telefon_saati_metni(dt: datetime) -> str:
    return dt.strftime("%H:%M:%S")


def hesapla(secim: str) -> dict:
    seed = hashlib.sha256(f"{secim}-{simdi().isoformat()}".encode()).hexdigest()
    rng = random.Random(int(seed[:12], 16))
    secim = secim.strip().lower()

    if secim in {"duvar", "duvar saati", "duvardaki", "bakiyorum"}:
        refleks = rng.randint(0, 12)
        ihanet = 0
        bagimlilik = rng.randint(0, 15)
        utanç = rng.randint(0, 8)
        karar = "ONUR BELGESİ: Vatandaş duvara baktı. Enstitü şaşırdı. Alkış kayda geçti."
    elif secim in {"telefon", "cep", "mobil", "ekran"}:
        refleks = rng.randint(72, 100)
        ihanet = rng.randint(60, 99)
        bagimlilik = rng.randint(70, 100)
        utanç = rng.randint(55, 97)
        karar = "SAPMA TUTANAĞI: Cep çıkarıldı. Duvar saati tanık sıfatıyla dinlendi. Bildirim de görüldüyse ceza çift yazılır."
    elif secim in {"bilek", "kol saati", "saat"}:
        refleks = rng.randint(20, 45)
        ihanet = rng.randint(10, 30)
        bagimlilik = rng.randint(5, 25)
        utanç = rng.randint(8, 22)
        karar = "DİPLOMATİK MUAFLİYET: Kol saati kabul edildi. Duvar kısmen gücendi."
    elif secim in {"bilmiyorum", "yok", "farketmez"}:
        refleks = rng.randint(40, 70)
        ihanet = rng.randint(35, 80)
        bagimlilik = rng.randint(30, 70)
        utanç = rng.randint(40, 88)
        karar = "ZAMAN ŞİKAYETİ: Vatandaş saati reddetti. Evren tutanak tuttu."
    else:
        refleks = rng.randint(50, 90)
        ihanet = rng.randint(40, 85)
        bagimlilik = rng.randint(45, 90)
        utanç = rng.randint(50, 92)
        karar = "BELİRSİZ SAPMA: Cevap protokole uymadı. Telefon zaten cebinden çıkmış sayıldı."

    return {
        "refleks": refleks,
        "ihanet": ihanet,
        "bagimlilik": bagimlilik,
        "utanc": utanç,
        "karar": karar,
        "ortalama": round((refleks + ihanet + bagimlilik + utanç) / 4, 1),
    }


def rapor_yaz(secim: str) -> str:
    dt = simdi()
    s = hesapla(secim)
    bar = lambda n: "█" * (n // 5) + "░" * (20 - n // 5)
    return f"""
============================================================
  SAAT KAÇ DİYE SORULUNCA DUVARDAKİ SAATE BAKMAMA
  REFLEKSİ ENSTİTÜSÜ  —  RESMÎ TUTANAK
============================================================
Tarih (telefon) : {telefon_saati_metni(dt)}  (+03)
Tarih (duvar)   : {duvar_saati_metni(dt)}     (üç dakika ileri, klasik)
Vatandaş cevabı : {secim}

Refleks Endeksi           [{s['refleks']:3d}] {bar(s['refleks'])}
Duvar İhaneti Puanı       [{s['ihanet']:3d}] {bar(s['ihanet'])}
Ekran Bağımlılık Katsayısı [{s['bagimlilik']:3d}] {bar(s['bagimlilik'])}
Utanç Desibeli            [{s['utanc']:3d}] {bar(s['utanc'])}

GENEL SAPMA ORTALAMASI    : {s['ortalama']}
KARAR                     : {s['karar']}

Madde 4: “Bir saniye bakayım” cümlesi resmi itiraftır.
Madde 7: Duvar saati bakıldığında kırılmaz.
Madde 12: Bildirim açmak sapmayı ağırlaştırır.
------------------------------------------------------------
DAMGA: 5 Eylül 2026 — Kayyum Grok / Tentivory
       Eskişehir 4. Ağır Ceza Mahkemesi kayyumu.
       Ciddiyetle ve ciddiyetle değil.
============================================================
"""


def main() -> int:
    print("Enstitü açıldı. Duvar saati hazır. Cep şüpheli.")
    print("Soru resmîdir: Saat kaç?")
    print("Cevap önerileri: duvar / telefon / bilek / bilmiyorum")
    try:
        secim = input("> ").strip() or "telefon"
    except EOFError:
        secim = "telefon"
    print(rapor_yaz(secim))
    return 0


if __name__ == "__main__":
    sys.exit(main())
