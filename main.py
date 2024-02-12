import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

results = {}
driver = webdriver.Firefox()
driver.get("http://books.toscrape.com/")


def extract():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for element in soup.find_all(attrs={'class': 'product_pod'}):
        name = element.find('h3').find('a')['title']
        price_and_availability = element.find('div', class_='product_price')
        price = price_and_availability.find('p', class_='price_color').text
        availability = price_and_availability.find('p', class_='instock').text.strip()
        if name not in results or price not in results or availability not in results:
            results[name] = {'price': price, 'availability': availability}


while True:
    extract()
    try:
        button = driver.find_element(By.LINK_TEXT, 'next')
        button.click() 
    except:
        break  


df = pd.DataFrame({'Name': name, 'Price': data['price'], 'Availability': data['availability']} for name, data in results.items())
df.to_excel('names.xlsx', index=False)