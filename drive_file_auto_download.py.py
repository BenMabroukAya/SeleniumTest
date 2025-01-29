from selenium import webdriver  # Importation de Selenium pour l'automatisation du navigateur
from selenium.webdriver.common.by import By  # Permet d'utiliser des sélecteurs pour localiser des éléments
from selenium.webdriver.support.ui import WebDriverWait  # Permet d'attendre qu'un élément soit présent
from selenium.webdriver.support import expected_conditions as EC  # Définit des conditions d'attente (ex. visibilité)
from selenium.webdriver.firefox.options import Options  # Permet de configurer les options du navigateur Firefox
from selenium.webdriver.firefox.service import Service  # Permet de définir le chemin du service geckodriver
import os  # Permet d'interagir avec le système de fichiers (créer des dossiers, vérifier les fichiers, etc.)

# Configuration des options pour Firefox
options = Options()  # Création d'un objet Options pour Firefox
download_dir = r"C:\Users\Aya\Downloads\test6.3"  # Dossier où le fichier sera téléchargé
os.makedirs(download_dir, exist_ok=True)  # Crée le dossier de téléchargement s'il n'existe pas

# Configuration des préférences de téléchargement dans Firefox
options.set_preference("browser.download.folderList", 2)  # Définit un dossier personnalisé pour les téléchargements
options.set_preference("browser.download.manager.showWhenStarting", False)  # Ne pas afficher la fenêtre du gestionnaire de téléchargement
options.set_preference("browser.download.dir", download_dir)  # Spécifie le dossier de téléchargement
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,image/jpeg,image/png,image/jpg")  # MIME types autorisés pour le téléchargement

# Définition du chemin d'accès au geckodriver (nécessaire pour utiliser Firefox avec Selenium)
service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')

# Initialisation du navigateur Firefox avec les options et le service définis
driver = webdriver.Firefox(service=service, options=options)

# Accès à l'URL du fichier Google Drive (ici un fichier spécifique)
driver.get("https://drive.google.com/file/d/1GycgRJa4ufCygN6lfBnuqGp1RG2NYaIt/view?usp=drive_link")

try:
    # Construction de l'URL de téléchargement direct
    file_url = "https://drive.google.com/uc?export=download&id=1GycgRJa4ufCygN6lfBnuqGp1RG2NYaIt"
    
    # Accès à l'URL de téléchargement direct
    driver.get(file_url)
    
    # Attente jusqu'à ce que le fichier soit téléchargé
    WebDriverWait(driver, 30).until(
        lambda d: os.path.exists(os.path.join(download_dir, "nom_du_fichier.jpg"))  # Remplacez par le nom exact du fichier attendu
    )
    print("Téléchargement terminé avec succès !")  # Message de succès lorsque le fichier est téléchargé

except Exception as e:  # Gestion des erreurs
    print(f"Une erreur s'est produite : {e}")

finally:
    driver.quit()  # Fermeture du navigateur après l'exécution
