from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Remplacez le chemin par celui de votre geckodriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Configuration des options
options = Options()
options.headless = False  # Pour afficher le navigateur

# Initialisation du navigateur Firefox avec les options et le service
driver = webdriver.Firefox(service=service, options=options)

# Ouvrir la page
driver.get("https://www.example.com")

# Exécuter un script JavaScript (alert)
driver.execute_script("alert('Hello from Selenium');")

# Attendre que l'alerte apparaisse et la fermer
time.sleep(2)  # Temps pour que l'alerte soit visible
driver.switch_to.alert.accept()  # Accepter (fermer) l'alerte

# Récupérer le titre de la page
title = driver.execute_script("return document.title;")
print(title)  # Afficher le titre de la page dans la console

# Quitter le navigateur
driver.quit()
