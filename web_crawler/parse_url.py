from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Firefox()

url = "https://www.gnc.com/prenatal/214312.html"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
file = "product.html"
with open(file, "w") as f:
    f.write(soup.prettify())

