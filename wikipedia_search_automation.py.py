"""
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By 


# Spécifiez le chemin vers GeckoDriver
service = Service('C:\\Users\\Aya\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe')

# Initialisez le WebDriver avec le service
driver = webdriver.Firefox(service=service)

driver.get("https://www.wikipedia.org/")

# Trouver un élément par son ID
element = driver.find_element(By.ID, "element_id")
element.click()

# Trouver un élément par son nom
element = driver.find_element(By.ID, "searchInput")
element.send_keys("Selenium")


# Soumettre un formulaire
element.submit()

driver.quit()
"""
"""""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')
driver = webdriver.Firefox(service=service)

try:
    driver.get("https://www.wikipedia.org/")
    # Trouver un élément par son ID
    element = driver.find_element(By.ID, "searchInput")
    element.send_keys("Selenium")
    # Soumettre le formulaire
    element.submit()
except NoSuchElementException as e:
    print(f"Erreur : {e}")
finally:
    driver.quit()
"""""


# Importation des modules nécessaires depuis Selenium
from selenium import webdriver  # Pour manipuler un navigateur web via WebDriver
from selenium.webdriver.firefox.service import Service  # Pour configurer le service du WebDriver (ici, Firefox)
from selenium.webdriver.common.by import By  # Pour spécifier les méthodes de recherche d'éléments dans le DOM
from selenium.common.exceptions import NoSuchElementException  # Pour gérer les exceptions lorsque des éléments ne sont pas trouvés

import time  # Importation du module time pour introduire des délais

# Configuration du service pour le pilote Firefox en spécifiant le chemin de geckodriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Initialisation d'une instance de WebDriver pour Firefox
driver = webdriver.Firefox(service=service)

try:
    # Charger la page d'accueil de Wikipédia
    driver.get("https://www.wikipedia.org/")
    
    # Trouver l'élément de recherche par son attribut ID dans le DOM
    element = driver.find_element(By.ID, "searchInput")
    
    # Entrer le texte "Selenium" dans le champ de recherche
    element.send_keys("Selenium")
    
    # Soumettre le formulaire pour rechercher le terme "Selenium"
    element.submit()
    
    # Pause pour laisser la page rester ouverte 2 minutes (120 secondes)
    time.sleep(120)
    
except NoSuchElementException as e:
    # Gérer les cas où un élément ne peut pas être trouvé et afficher un message d'erreur
    print(f"Erreur : {e}")
    
finally:
    # Fermer le navigateur et libérer les ressources
    driver.quit()
