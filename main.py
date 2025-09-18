from selenium import webdriver 
from selenium.webdriver.edge.service import Service 
from time import sleep 
 
service = Service(executable_path='C:\edgedriver\msedgedriver.exe') 
options = webdriver.EdgeOptions() 
driver = webdriver.Edge(service=service, options=options) 
driver.get("https://www.linkedin.com/pulse/selenium-un-guide-exhaustif-pourlautomatisation-des-tests-barta/") 
sleep(10) 
driver.quit()