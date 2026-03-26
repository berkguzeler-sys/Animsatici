import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

def mail_gonder(konu, icerik):
    gonderen_mail = "bg.guzeler@gmail.com"
    sifre = "fayflwijkpgthnxl"

    alici_mail = "yonetim@polipediasigorta.com"

    mesaj = MIMEText(icerik)
    mesaj["Subject"] = konu
    mesaj["From"] = gonderen_mail
    mesaj["To"] = alici_mail

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gonderen_mail, sifre)
    server.send_message(mesaj)
    server.quit()

    print(f"{konu} gönderildi")


odemeler = {
    5:  "Polipedia İşbankası Kredi Kartı Ödemesi",
    15: "Maestro Araç Taksit Ödemesi",
    20: "Ofis Kira Ödemesi",
    23: "Vakıfbank Maestro Kredi Kartı Ödemesi",
    30: "Maaş, Ticketi, Vergi, SSK ödemesi"
}

while True:
    bugun = datetime.now().day

    if bugun in odemeler:
        konu = odemeler[bugun]
        icerik = f"Hatırlatma: {konu}"

        mail_gonder(konu, icerik)

        time.sleep(86400)  # 1 gün bekle

    time.sleep(3600)  # saatlik kontrol
