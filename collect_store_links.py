import os
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# Get the current directory path
current_directory = os.getcwd()

# Specify the additional path to the Chrome profile
chrome_profile_path = "/chrome/data/profile/Default"

# Join the current directory path with the provided Chrome profile path
full_chrome_profile_path = os.path.join(current_directory, chrome_profile_path)

chrome_options.add_argument("user-data-dir=" + full_chrome_profile_path)
browser = uc.Chrome(driver_executable_path='chromedriver.exe', browser_executable_path='chrome/chrome.exe', options=chrome_options)

browser.get('https://www.tripadvisor.com/Restaurants-g147289-Santo_Domingo_Santo_Domingo_Province_Dominican_Republic.html')
all_urls = browser.find_elements(By.TAG_NAME, 'a')
all_restaurant_links = []
for url in all_urls:
    link = url.get_attribute('href')
    if 'Restaurant_Review-' in link and not '.html#REVIEWS' in link:
        all_restaurant_links.append(link)
    if 'Next page' in url.get_attribute('aria-label'):
        browser.get(link)
        break
        
all_restaurant_links = list(set(all_restaurant_links))
print(len(all_restaurant_links))
print(all_restaurant_links)

time.sleep(20)