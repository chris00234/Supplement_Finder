from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.gnc.com/vitamins-supplements/?start=0&sz=1260&sizeAdjusted=true"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
file = "gnc.html"
with open(file, "w") as f:
    f.write(soup.prettify())
