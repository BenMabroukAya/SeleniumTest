from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Remplacez le chemin par celui de votre geckodriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Configuration des options pour Firefox
options = Options()
options.headless = False  # Pour afficher le navigateur

# Initialisation du navigateur Firefox avec les options et le service
driver = webdriver.Firefox(service=service, options=options)

# Ouvrir la page web
driver.get("https://www.example.com")

# Attendre que la page soit complètement chargée avant de prendre la capture d'écran
time.sleep(2)  # Attendre 2 secondes pour être sûr que la page est prête

# Capturer une capture d'écran de la page entière et l'enregistrer dans le dossier spécifié
driver.save_screenshot('C:/Users/Aya/Pictures/screenshot.png')  # Capture d'écran de la page entière

# Capturer une capture d'écran de l'élément <h1> (Example Domain)
try:
    element = driver.find_element(By.TAG_NAME, "h1")  # Recherche l'élément <h1>
    element.screenshot('C:/Users/Aya/Pictures/h1_screenshot.png')  # Capture d'écran de l'élément <h1>
except Exception as e:
    print("L'élément n'a pas été trouvé :", e)

# Quitter le navigateur
driver.quit()
