from selenium import webdriver  # Importe Selenium pour automatiser un navigateur web
from selenium.webdriver.firefox.service import Service  # Permet de spécifier un service pour le pilote GeckoDriver
from selenium.webdriver.common.by import By  # Fournit des options pour localiser des éléments (par ID, NAME, etc.)
import time  # Importe le module time pour gérer les pauses dans le script

# Spécifiez le chemin vers GeckoDriver (navigateur Firefox)
service = Service('geckodriver.exe')  # Remplacez par le chemin exact du fichier GeckoDriver

# Initialisez le WebDriver pour interagir avec Firefox en utilisant le service défini
driver = webdriver.Firefox(service=service)

# Étape 1 : Connexion au site WordPress
driver.get("http://localhost/mysite/login/")  # Charge la page de connexion

# Localiser le champ pour le nom d'utilisateur (attribut name='log')
login = driver.find_element(By.NAME, 'log')
user = "Iam_Bot"  # Définir le nom d'utilisateur
login.send_keys(user)  # Saisir le nom d'utilisateur dans le champ

# Localiser le champ pour le mot de passe (attribut name='pwd')
password = driver.find_element(By.NAME, 'pwd')
passBot = "IamBot&2024"  # Définir le mot de passe
password.send_keys(passBot)  # Saisir le mot de passe dans le champ

# Localiser le bouton de soumission (attribut name='submit')
submit_btn = driver.find_element(By.NAME, 'submit')
submit_btn.click()  # Simuler un clic pour se connecter

# Pause pour permettre le chargement de la page après la connexion
time.sleep(7)

# Étape 2 : Accéder à une page d'article spécifique
driver.get("http://localhost/mysite/langage-php/")  # Charge la page d'un article spécifique
time.sleep(5)  # Pause pour s'assurer que la page est complètement chargée

# Étape 3 : Ajouter un commentaire
# Localiser le champ de texte pour le commentaire (vérifiez l'ID ou le sélecteur CSS si besoin)
comment_field = driver.find_element(By.ID, 'comment')  # ID du champ de commentaire
comment_text = "Ceci est un commentaire posté par un bot."  # Définir le contenu du commentaire
comment_field.send_keys(comment_text)  # Saisir le texte dans le champ de commentaire

# Localiser le bouton de soumission du commentaire (vérifiez l'ID ou le sélecteur CSS si besoin)
submit_comment = driver.find_element(By.ID, 'submit')  # ID du bouton de soumission
submit_comment.click()  # Simuler un clic pour soumettre le commentaire

# Pause pour permettre le traitement après la soumission
time.sleep(5)

# Étape finale : Fermer le navigateur
driver.quit()  # Ferme le navigateur et termine la session WebDriver
