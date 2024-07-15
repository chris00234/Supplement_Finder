from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from fake_useragent import UserAgent
import undetected_chromedriver as uc

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f"user-agent={get_random_user_agent()}")
    driver = uc.Chrome(options=options)
    return driver

def fetching_ingredient(file):
    file2 = "product.html"
    product_dict = {}
    with open(file, "r") as f:
        with open(file2, "w") as f2:
            line = f.readline()
            while line:
                line_ = line.split(' ')
                url = line_[0]
                title = "".join(line_[1:])

                driver = get_driver()
                driver.get(url)
                time.sleep(random.uniform(3, 7))  # More random sleep time
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tb = soup.find_all("td", class_="data")
                ingredients = []
                for td in tb:
                    if td.find('b') or td.find('strong'):
                        continue
                    # Extract ingredient name
                    ingredient_name = td.get_text(strip=True)
                    amount_per_serving = ""

                    next_td = td.find_next_sibling("td", class_="data")
                    if next_td:
                        amount_per_serving = next_td.get_text(strip=True)
                    
                    if ingredient_name:
                        ingredients.append(f"{ingredient_name}: {amount_per_serving}")
                
                print(ingredients)
                # f2.write(url + " " + title + '\n')
                # f2.write(str(tb))
                # f2.write('\n\n')
                driver.quit()
                line = f.readline()
            f2.write(product_dict)

def main():
    file = "all_url.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()