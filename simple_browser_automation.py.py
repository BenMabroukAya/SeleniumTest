from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

# Spécifiez le chemin vers GeckoDriver
service = Service('geckodriver.exe')

# Initialisez le WebDriver avec le service
driver = webdriver.Firefox(service=service)

driver.get("https://www.wikipedia.org/")
print(driver.title)

# Attendez quelques secondes
time.sleep(10)

driver.quit()
"""
Cet exemple ouvre la page d'accueil de wikipedia.org 
sur FireFox pendant 10 secondes"""