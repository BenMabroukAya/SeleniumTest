import unittest  # Importation du module unittest pour créer et exécuter des tests unitaires
from selenium import webdriver  # Importation de webdriver pour contrôler un navigateur avec Selenium
from selenium.webdriver.firefox.service import Service  # Importation de Service pour spécifier le chemin vers geckodriver
import time  # Importation du module time pour utiliser sleep

class TestExample(unittest.TestCase):  # Définition de la classe de test qui hérite de unittest.TestCase
    def setUp(self):  # Méthode d'initialisation, appelée avant chaque test
        # Créer un objet Service pour spécifier le chemin de geckodriver
        service = Service('C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')
        # Initialisation du navigateur Firefox avec le service
        self.driver = webdriver.Firefox(service=service)

    def test_example(self):  # Méthode de test, contenant le code du test réel
        self.driver.get("https://www.example.com")  # Ouvrir la page "https://www.example.com"
        # Vérifier que le titre de la page contient "Example Domain"
        self.assertIn("aya", self.driver.title)

    def tearDown(self):  # Méthode de nettoyage, appelée après chaque test
        time.sleep(2)  # Ajouter un délai de 2 secondes pour garder le navigateur ouvert
        self.driver.quit()  # Fermer le navigateur après le test

if __name__ == "__main__":  # Condition qui s'assure que le script soit exécuté directement
    unittest.main()  # Exécuter tous les tests définis dans la classe TestExample
