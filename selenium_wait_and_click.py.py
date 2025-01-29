from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path='C:/Users/Aya/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe')
driver.get("https://www.tresfacile.net/login/")

# Attendre que l'élément soit cliquable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "element_id"))
    )
    element.click()
finally:
    driver.quit()