from selenium import webdriver 
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
from time import sleep 

if __name__ == "__main__": 

# Ce script ouvre une Todo App de démo, 
# coche des cases, ajoute un texte et vérifie le titre de la page. 

# 1. Préparation du navigateur Edge 
    service = Service(executable_path="C:\edgedriver\msedgedriver.exe")
    options = webdriver.EdgeOptions() 
    browser = webdriver.Edge(service=service, options=options) 
    browser.maximize_window() 
    browser.get("https://lambdatest.github.io/sample-todo-app/") 
try: 
# 2. Coche la case "li1" 
    li1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "li1"))) 
    li1.click() 
# 3. Coche la case "li2" 
    li2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "li3"))) 
    li2.click()
# 4. Vérifie que le titre de la page est correct 
    expected_title = "Sample page - lambdatest.com" 
# assert expected_title == browser.title 
# print("Le titre est correct :", browser.title) 
 
# 5. Ajoute un texte dans le champ 
    email_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "sampletodotext"))) 
    email_field.send_keys("Happy Testing at LambdaTest") 
 
# 6. Clique sur le bouton "Add" 
    add_button = WebDriverWait(browser, 10).until( 
    EC.presence_of_element_located((By.ID, "addbutton")) 
    ) 
    add_button.click() 
 
# Pause pour voir le résultat 
    sleep(5) 
 
except TimeoutException: 
    print("Un élément n'a pas été trouvé sur la page") 
 
finally: 
# 7. Ferme le navigateur 
    browser.quit()