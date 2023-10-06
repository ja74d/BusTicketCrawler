from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Set up the Chrome WebDriver with headless mode
chrome_options = ChromeOptions()
chrome_options.headless = True

# Replace 'chromedriver_path' with the path to your Chrome WebDriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=chromedriver_path), options=chrome_options)




# Replace 'https://example.com' with the URL you want to scrape
url = 'https://safar724.com/bus/kermanshah-esfahan?date=1402-7-21'

# Load the web page using Selenium
driver.get(url)



time.sleep(5)

# Wait for a certain element to appear (adjust timeout as needed)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#Services')))

# Get the page source after it has fully loaded
page_source = driver.page_source

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

tabl = soup.find('div', id='Services')

ticket = tabl.find_all('script')

for x in ticket:
    print(x.string)
