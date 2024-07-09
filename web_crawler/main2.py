from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.gnc.com/multivitamins-for-men/201412.html#q=multivitamin&start=1"
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
file = "gnc.html"
with open(file, "w") as f:
    f.write(soup.prettify())
