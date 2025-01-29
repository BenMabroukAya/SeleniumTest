from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Spécifiez le chemin vers GeckoDriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Initialisez le WebDriver avec le service
driver = webdriver.Firefox(service=service)

# Accéder à la page de connexion de votre site "Eshopify"
driver.get("http://localhost/mysite/Eshopify/cnx.php")

# Rechercher et remplir le champ user_login
login = driver.find_element(By.NAME, 'email')
user = "iambot@gmail.com"
login.send_keys(user)

# Rechercher et remplir le champ password
password = driver.find_element(By.NAME, 'password')
passBot = "IamBot&2024"
password.send_keys(passBot)

# Rechercher et cliquer sur le bouton de soumission
submit_btn = driver.find_element(By.NAME, 'login')
submit_btn.click()

# Attendre pour permettre le chargement des pages
time.sleep(7)

# Accéder au tableau de bord
driver.get("http://localhost/mysite/Eshopify/admin.php")

time.sleep(15)

# Accéder à la page d'accueil
driver.get("http://localhost/mysite/Eshopify/index.php")

time.sleep(15)

# Accéder à la page des produits
driver.get("http://localhost/mysite/Eshopify/products.php")

time.sleep(15)

# Accéder à la page de contact
driver.get("http://localhost/mysite/Eshopify/contact.php")

time.sleep(15)

# Accéder à la page about us
driver.get("http://localhost/mysite/Eshopify/about.php")

time.sleep(15)

# Fermer le navigateur
driver.quit()
