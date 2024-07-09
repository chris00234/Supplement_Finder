from bs4 import BeautifulSoup
from selenium import webdriver

def fetching_ingredient(file):
    with open(file, "r") as f:
        line = f.readline()
        driver = webdriver.Firefox()
        while line:
            driver.get(line)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            print(soup.prettify())
            line = f.readline()
        driver.quit()

def main():
    file = "url_only.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()