from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def get_driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f"user-agent={get_random_user_agent()}")
    options.add_argument("--enable-javascript")

    driver = webdriver.Chrome(options=options)
    return driver

def simulate_click_and_hold(driver):
    width = driver.execute_script("return window.innerWidth")
    height = driver.execute_script("return window.innerHeight")

    center_x = width //2
    center_y = height//2

    actions = ActionChains(driver)
    actions.move_by_offset(center_x, center_y).click_and_hold().pause(1).release().perform()
    actions.move_by_offset(-center_x, -center_y).perform()


def fetching_ingredient(file):
    file2 = "products.html"
    with open(file, "r") as f:
        with open(file2, "w") as f2:
            line = f.readline()
            while line:
                driver = get_driver()
                driver.get(line)

                time.sleep(random.uniform(25,30))

                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                except:
                    simulate_click_and_hold(driver)
                    time.sleep(20)
                    
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tb = soup.find_all("td",class_="data")

                print(tb)
                f2.write(str(tb) + "\n")
                    
                line = f.readline()
        driver.quit()

def main():
    file = "url_only.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()