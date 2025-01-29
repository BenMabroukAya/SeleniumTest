# Importation des modules nécessaires de Selenium et de time
from selenium import webdriver  # Pour contrôler le navigateur avec Selenium
from selenium.webdriver.firefox.service import Service  # Pour spécifier le service GeckoDriver pour Firefox
from selenium.webdriver.common.by import By  # Pour localiser des éléments sur la page
import time  # Pour gérer les pauses temporaires (attente explicite en secondes)

# Spécifiez le chemin vers GeckoDriver (nécessaire pour utiliser Firefox avec Selenium)
service  = Service('geckodriver.exe')  # Le chemin de GeckoDriver. Ici, il est supposé être dans le même dossier que le script.

# Initialisez le WebDriver avec le service spécifié
driver = webdriver.Firefox(service=service)  # Lancement de Firefox avec Selenium et le service GeckoDriver

# Ouvrir l'URL de la page d'enregistrement des utilisateurs
driver.get("http://localhost/mysite/register/")  # Charge la page de registre des utilisateurs localement

# Trouver le champ 'user_login' et remplir avec le nom d'utilisateur
login = driver.find_element(By.NAME, 'user_login')  # Recherche de l'élément avec l'attribut 'name' égal à 'user_login'
username = 'Iam_Bot'  # Définir le nom d'utilisateur à envoyer
login.send_keys(username)  # Envoi du nom d'utilisateur dans le champ de texte

# Trouver le champ 'user_email' et remplir avec l'adresse e-mail
email = driver.find_element(By.NAME, 'user_email')  # Recherche de l'élément avec l'attribut 'name' égal à 'user_email'
email_value = 'iambot@gmail.com'  # Définir l'adresse e-mail à envoyer
email.send_keys(email_value)  # Envoi de l'adresse e-mail dans le champ de texte

# Trouver le champ 'user_pass1' et remplir avec le mot de passe
password1 = driver.find_element(By.NAME, 'user_pass1')  # Recherche de l'élément avec l'attribut 'name' égal à 'user_pass1'
pass1 = 'IamBot&2024'  # Définir le mot de passe à envoyer
password1.send_keys(pass1)  # Envoi du mot de passe dans le champ de texte

# Trouver le champ 'user_pass2' et remplir avec le mot de passe de confirmation
password2 = driver.find_element(By.NAME, 'user_pass2')  # Recherche de l'élément avec l'attribut 'name' égal à 'user_pass2'
pass2 = 'IamBot&2024'  # Le mot de passe de confirmation est le même que le mot de passe
password2.send_keys(pass2)  # Envoi du mot de passe de confirmation dans le champ de texte

# Trouver le bouton de soumission et cliquer dessus pour soumettre le formulaire
submit_login = driver.find_element(By.NAME, "submit")  # Recherche du bouton avec l'attribut 'name' égal à 'submit'
submit_login.click()  # Clique sur le bouton pour soumettre le formulaire d'enregistrement

# Attendre quelques secondes pour que la page suivante se charge complètement
time.sleep(10)  # Pause de 10 secondes pour permettre à la page de se charger

# Accéder à la page du tableau de bord après l'enregistrement
driver.get("http://localhost/mysite/dashboard/")  # Ouvre l'URL du tableau de bord de l'utilisateur

# Rester quelques secondes sur la page du tableau de bord
time.sleep(10)  # Pause de 10 secondes pour examiner la page du tableau de bord

# Fermer le navigateur une fois l'opération terminée
driver.close()  # Ferme la fenêtre du navigateur contrôlée par Selenium
