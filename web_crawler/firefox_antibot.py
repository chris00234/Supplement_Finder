# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# import time
# import random
# from fake_useragent import UserAgent




# def get_random_user_agent():
#     ua = UserAgent()
#     return ua.random

# def get_driver():
    
    
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument(f"user-agent={get_random_user_agent()}")
#     driver = webdriver.Firefox(options=options)
#     return driver


# def fetching_ingredient(file):
#     file2 = "products.html"
#     with open(file, "r") as f:
#         with open(file2, "w") as f2:
#             line = f.readline()
#             while line:
#                 driver = get_driver()
#                 driver.get(line)
#                 time.sleep(random.uniform(1,5))
#                 soup = BeautifulSoup(driver.page_source, 'html.parser')
#                 tb = soup.find_all("td",class_="data")
#                 f2.write(str(tb))
                    
#                 line = f.readline()
#         driver.quit()



# def main():
#     file = "url_only.txt"
#     fetching_ingredient(file)

# if __name__ == '__main__':
#     main()

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
import random
from fake_useragent import UserAgent
# import undetected_chromedriver as uc

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={get_random_user_agent()}")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def fetching_ingredient(file):
    file2 = "products.html"
    with open(file, "r") as f:
        with open(file2, "w") as f2:
            line = f.readline()
            while line:
                driver = get_driver()
                driver.get(line)
                time.sleep(random.uniform(3, 7))  # More random sleep time
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tb = soup.find_all("td", class_="data")
                print(tb)
                f2.write(str(tb))
                driver.quit()
                line = f.readline()

def main():
    file = "url_only.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()
