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
url = 'https://www.payaneha.com/busticket/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%A8%D9%84%DB%8C%D8%B7-%D8%A7%D8%AA%D9%88%D8%A8%D9%88%D8%B3-%D8%A7%D8%B2-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-%D8%A8%D9%87-%DA%A9%D8%B1%D9%85%D8%A7%D9%86%D8%B4%D8%A7%D9%87'


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
