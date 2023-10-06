from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


headers = {"User-Agent": UserAgent().random}
source = requests.get(
    'https://www.payaneha.com/busticket/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%A8%D9%84%DB%8C%D8%B7-%D8%A7%D8%AA%D9%88%D8%A8%D9%88%D8%B3-%D8%A7%D8%B2-%D8%A7%D8%B5%D9%81%D9%87%D8%A7%D9%86-%D8%A8%D9%87-%DA%A9%D8%B1%D9%85%D8%A7%D9%86%D8%B4%D8%A7%D9%87', 
    headers=headers, 
    timeout=100).text
source.raise_for_status()

soup = BeautifulSoup(source, 'lxml')

buses = soup.find_all('div', id='result_wrapper-font13')

print(buses)