import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Spécifiez le chemin vers le geckodriver pour Firefox
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')
driver = webdriver.Firefox(service=service)

# Ouvrir un nouvel onglet et charger une URL spécifique
driver.execute_script("window.open('https://www.google.com', '_blank');")  
# La méthode `execute_script` exécute du JavaScript pour ouvrir un nouvel onglet avec Google.

# Passer au nouvel onglet (le deuxième onglet dans `window_handles`, index 1)
driver.switch_to.window(driver.window_handles[1])  
# `window_handles` retourne une liste des identifiants de tous les onglets ouverts.
# On sélectionne le deuxième onglet (index 1).

# Afficher le titre de l'onglet actif
print(driver.title)  
# Affiche le titre de la page actuellement chargée pour vérifier que l'onglet actif est bien Google.

# Pause de 5 secondes pour observer le navigateur
print("Pause de 5 secondes. Vérifiez le navigateur.")
time.sleep(5)  # Pause de 5 secondes

# Fermer l'onglet actif
driver.close()  
# Ferme l'onglet où le focus est actuellement.

# Revenir au premier onglet (index 0 dans `window_handles`)
driver.switch_to.window(driver.window_handles[0])  
# On revient au premier onglet initial.

# Afficher le titre de l'onglet initial
print(driver.title)  
# Affiche le titre de la page initiale pour confirmer le retour au premier onglet.

# Pause supplémentaire de 5 secondes pour observer le premier onglet avant de quitter
print("Pause de 5 secondes pour observer le premier onglet.")
time.sleep(5)  # Pause de 5 secondes

# Quitter le navigateur
driver.quit()
