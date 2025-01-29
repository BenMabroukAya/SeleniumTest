from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time  # Importer le module time pour utiliser sleep

# Spécifiez le chemin de votre geckodriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Configuration des options pour Firefox
options = Options()
options.headless = False  # Défini à False pour afficher le navigateur (True pour mode sans tête)

# Initialisation du navigateur Firefox avec les options et le service
driver = webdriver.Firefox(service=service, options=options)

# Ouvrir la page web
driver.get("https://www.example.com")

# Ajouter un cookie
driver.add_cookie({"name": "key", "value": "value"})

# Obtenir un cookie
cookie = driver.get_cookie("key")
print(cookie)  # Affiche le cookie récupéré

# Attendre un peu pour garder la page ouverte
time.sleep(3)  # Attendre 5 secondes

# Supprimer un cookie
driver.delete_cookie("key")

# Supprimer tous les cookies
driver.delete_all_cookies()

# Quitter le navigateur après un délai
driver.quit()
