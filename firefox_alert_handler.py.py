import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Spécifiez le chemin vers le geckodriver pour Firefox
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Initialisation du driver Firefox
driver = webdriver.Firefox(service=service)

# Ouvrir la page example.com
driver.get('http://example.com')

# Pause pour s'assurer que la page est complètement chargée (à ajuster selon les besoins)
time.sleep(2)

# Ajouter un script JavaScript pour déclencher une alerte
driver.execute_script('alert("Ceci est une alerte de test !");')

# Pause pour s'assurer que l'alerte est affichée
time.sleep(5)

# Gérer l'alerte
try:
    # Passer à l'alerte active
    alert = driver.switch_to.alert

    # Lire le texte de l'alerte
    print("Texte de l'alerte : ", alert.text)

    # Accepter l'alerte
    alert.accept()
    print("Alerte acceptée.")

    # Vous pouvez aussi tester le rejet de l'alerte (si vous voulez)
    # alert.
    # dismiss()
    # print("Alerte refusée.")

except Exception as e:
    print("Erreur lors de la gestion de l'alerte : ", e)

# Fermer le navigateur
driver.quit()
