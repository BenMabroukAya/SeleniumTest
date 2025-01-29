import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Spécifiez le chemin vers le geckodriver pour Firefox
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Initialisation du driver Firefox
driver = webdriver.Firefox(service=service)

# Ouvrir une page (ajoutez l'URL appropriée ici)
driver.get('http://example.com')  # Remplacez par l'URL de votre choix

# Pause pour s'assurer que la page est complètement chargée (à ajuster selon les besoins)
time.sleep(10)

# Attendre et gérer les alertes
try:
    # Passer à l'alerte active
    alert = driver.switch_to.alert

    # Accepter l'alerte
    alert.accept()
    print("Alerte acceptée.")

    # Refuser une alerte (si elle est présente)
    # Attention : l'alerte doit être déclenchée avant de pouvoir la rejeter
    alert = driver.switch_to.alert  # Assurez-vous de pointer vers la bonne alerte
    alert.dismiss()
    print("Alerte refusée.")

    # Lire le texte de l'alerte
    print("Texte de l'alerte : ", alert.text)

    # Entrer du texte dans une alerte (si l'alerte permet l'entrée de texte)
    alert.send_keys("Selenium")
    alert.accept()
    print("Texte envoyé et alerte acceptée.")

except Exception as e:
    print("Aucune alerte trouvée ou erreur :", e)

# Fermer le navigateur
driver.quit()
