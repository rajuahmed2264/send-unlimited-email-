import json
import re
import time
import os
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from generate_email_body import generate_body
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def clean_email(email):
    allowed_chars = re.compile(r'[^a-zA-Z0-9._@]')
    cleaned_email = allowed_chars.sub('', email)
    return cleaned_email

while True:
    with open('calculationdata.json', 'r') as file:
        data = json.load(file)
    browser_no = int(data['browser_no'])
    account_no = int(data['account_no'])
    total_sent = int(data['total_sent'])
    if total_sent==1001:
        break
# Determine the correct profile path based on browser_no
    if browser_no == 0:
        chrome_profile_path = os.path.join("chrome", "data", "profile", "Default")
    elif browser_no == 1:
        chrome_profile_path = os.path.join("chrome", "data", "profile", "Profile 1")
    else:
        browser_no += 1
        chrome_profile_path = os.path.join("chrome", "data", "profile", f"Profile {browser_no}")

    
    chrome_options = webdriver.ChromeOptions()
    # Get the current directory path
    current_directory = os.getcwd()
    full_chrome_profile_path = os.path.join(current_directory, chrome_profile_path)

    chrome_options.add_argument("user-data-dir=" + full_chrome_profile_path)
    browser = uc.Chrome(driver_executable_path='chromedriver.exe', browser_executable_path='chrome/chrome.exe', options=chrome_options)
    browser.maximize_window()
    while True:
        url = f"https://mail.google.com/mail/u/{account_no}/?tab=rm&ogbl#inbox?compose=new"
        browser.get(url)
        with open('calculationdata.json', 'r') as file:
            data = json.load(file)
            browser_no = int(data['browser_no'])
            account_no = int(data['account_no'])
        account_no +=1
        if account_no >=11:
            file_path = 'calculationdata.json'
            # Update the `browser_no` value
            with open(file_path, 'r') as file:
                data = json.load(file)
            data['account_no'] = 0

            # Write the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            break
        else:
            try:
                lead_response = requests.get('https://mngdb.tidytechsolution.xyz/get_trusted_domain?ofst=0')
                lead_response.raise_for_status()  # Check for HTTP request errors
                lead = lead_response.json()
                receiver_email = lead[0][3]
                wait = WebDriverWait(browser, 120)  # Set the wait time
                receipent = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="To recipients"]')))

                # Handle status update logic here if necessary
                receipent.send_keys(receiver_email)

                subject_box = browser.find_element(By.NAME, 'subjectbox')
                excel_file_path = 'all_data.xlsx'
                sender_file_path = 'mails.xlsx'

                # Read data from Excel files
                all_dfs = pd.read_excel(excel_file_path, sheet_name=None)
                sender_name = ''
                html_content, mail_subject = generate_body(all_dfs=all_dfs, sender_name = sender_name)
                subject_box.send_keys(mail_subject)
                html_content = html_content.replace('\\n', '\n').replace('\\t', '\t')
                message_body = browser.execute_script('return document.querySelector(\'[aria-label="Message Body"]\').parentElement.parentElement.parentElement.lastElementChild.firstElementChild.firstElementChild;')
                
                browser.execute_script("arguments[0].innerText = arguments[1];", message_body,html_content )


                send_btn = browser.find_element(By.XPATH, "//div[@aria-label='Send ‪(Ctrl-Enter)‬']")
                send_btn.click()
                upid = lead[0][0]
                requests.get(f'https://mngdb.tidytechsolution.xyz/updt_sent_trusted?upid={upid}')

                wait = WebDriverWait(browser, 120)  # Set the wait time

                # Wait for the element with text "Message sent"
                message_sent_element = wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[text()="Message sent"]'))
                )
                time.sleep(5)

            except requests.RequestException as req_err:
                print(f"Request error: {req_err}")
            except Exception as e:
                print(f"An error occurred: {e}")
            file_path = 'calculationdata.json'
            # Update the `browser_no` value
            with open(file_path, 'r') as file:
                data = json.load(file)
            data['account_no'] = account_no
            total_sent = int(data['total_sent'])
            total_sent +=1
            data['total_sent'] = total_sent
            # Write the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
    browser.close()
