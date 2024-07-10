from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
from fake_useragent import UserAgent

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={get_random_user_agent()}")
    driver = webdriver.Firefox(options=options)
    return driver


def fetching_ingredient(file):
    file2 = "products.html"
    with open(file, "r") as f:
        with open(file2, "w") as f2:
            line = f.readline()
            while line:
                driver = get_driver()
                driver.get(line)
                time.sleep(random.uniform(1,5))
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tb = soup.find_all("td",class_="data")
                f2.write(tb)
                    
                line = f.readline()
        driver.quit()



def main():
    file = "url_only.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()