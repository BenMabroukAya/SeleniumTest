from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Spécifiez le chemin vers GeckoDriver
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')
# Initialisez le WebDriver avec le service
driver = webdriver.Firefox(service=service)

# Connexion au site WordPress
driver.get("http://localhost/mysite/Eshopify/cnx.php")
login = driver.find_element(By.NAME, 'email')
user = "iambot@gmail.com"
login.send_keys(user)
password = driver.find_element(By.NAME, 'password')
passBot = "IamBot&2024"
password.send_keys(passBot)
submit_btn = driver.find_element(By.NAME, 'submit')
submit_btn.click()

time.sleep(7)

# Aller à la page d'un article spécifique
driver.get("http://localhost/mysite/Eshopify/edit_product.php?id=74") 
time.sleep(5)

# Localiser le champ de texte pour le commentaire
comment_field = driver.find_element(By.ID, '74')  #
comment_text = "Ceci est un commentaire posté par un bot."
comment_field.send_keys(comment_text)

# Localiser et cliquer sur le bouton de soumission du commentaire
submit_comment = driver.find_element(By.ID, '74')  # L'ID ou le sélecteur peut varier
submit_comment.click()

time.sleep(5)

# Quitter le navigateur
driver.quit()