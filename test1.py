import csv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# CSV file paths
input_file = "input.csv"
output_file = "result.csv"

# WebDriver Initialization
service = Service(executable_path="C:\\edgedriver\\msedgedriver.exe")
options = webdriver.EdgeOptions()
browser = webdriver.Edge(service=service, options=options)

results = []

with open(input_file, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        num_case = row["Num_cas_test"]
        email = row["mail"]
        pwd = row["pwd"]

        browser.get("https://accounts.lambdatest.com/login")

        try:
            # email field
            email_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.clear()
            email_field.send_keys(email)

            # password field
            pwd_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            pwd_field.clear()
            pwd_field.send_keys(pwd)

            # login button
            login_btn = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "login-button"))
            )
            login_btn.click()

            sleep(3)

            # Check if login successful → e.g. dashboard presence
            try:
                WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.ID, "profile__dropdown")) # ID d’un élément après login
                )
                results.append([num_case, 1])  # Success
            except TimeoutException:
                results.append([num_case, 0])  # Failure

        except TimeoutException:
            print(f"Un élément n’a pas été trouvé pour le cas {num_case}")
            results.append([num_case, 0])

# Closing the browser
browser.quit()

# Writing results to output CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["Num_cas_test", "OK"])
    writer.writerows(results)

print("Test terminé. Résultats enregistrés dans", output_file)