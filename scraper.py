from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


class SteamScrapper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def get_data(self) -> str:
        STEAM_URL = "https://steamdb.info/graph/?sort=peak"
        self.driver.get(STEAM_URL)
        listings = self.driver.find_elements(By.CSS_SELECTOR, "table[id='table-apps'] tbody tr")
        file_name = "steam_peak.csv"
        with open(file_name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'peak'])
            for tr in listings:
                title = tr.find_elements(By.CSS_SELECTOR, "a")[1].text
                peak = int(tr.find_elements(By.CSS_SELECTOR, "td")[-2].text.replace(",", ""))
                writer.writerow([title, peak])
        return file_name

    def send_data_to_email(self, to_addr: str):
        file_name = self.get_data()

        msg = MIMEMultipart()
        msg["Subject"] = "Steam's top 100 according to peak player count!"
        msg["From"] = "jlee24281@gmail.com"
        msg["To"] = to_addr

        body = MIMEText('''
                        Please see attached to view top 100 listings of steam games
                    ''')
        msg.attach(body)

        fp = open(file_name, "rb")
        att = MIMEApplication(fp.read(), _subtype="csv")
        fp.close
        att.add_header("Content-Disposition", "attachment", filename = file_name)
        msg.attach(att)

        with smtplib.SMTP("smtp.gmail.com") as session:
            session.starttls()
            session.login(user="jlee24281@gmail.com", password="fdjdjbwngoyrdapn")
            session.sendmail(from_addr='jlee24281@gmail.com',to_addrs=to_addr, msg=msg.as_string())



