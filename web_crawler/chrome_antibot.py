from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import json
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
    file2 = "product.json"
    product_dict = {}
    num = 0
    with open(file, "r") as f:
        with open(file2, "a") as f2:
            line = f.readline()
            while line:
                line_ = line.split(' ')
                url = line_[0]
                title = "".join(line_[1:]).strip()
                
                driver = get_driver()
                driver.get(url)
                # time.sleep(random.uniform(3, 7))  # More random sleep time
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                tb = soup.find_all("td", class_="data", valign="top")
                ingredient = {}
                ing = ""
                for i in tb:
                    if str(i).startswith("<td class=\"data\" valign=\"top\">"):
                        ing = i.get_text().strip()
                        ingredient[i.get_text().strip()] = ""
                    elif ing == "":
                        print("fuck")
                        break
                    elif str(i).startswith("<td align=\"right\" class=\"data\" nowrap=\"nowrap\" valign=\"top\">") and not i.get_text().endswith("%") and ingredient[ing] == "":
                        ingredient[ing] = i.get_text().strip()
                    elif str(i).startswith("<td align=\"right\" class=\"data\" valign=\"top\">") and ingredient[ing] == "":
                        ingredient[ing] = i.get_text().strip()
                product_dict[title] = ingredient
                # print(product_dict[title])
                # print("--" * 50)
                driver.quit()
                line = f.readline()
                num += 1
                print(f"current url num = #{num}")
                if num % 30 == 0:
                    json.dump(product_dict,f2, indent=4)
            
            

    # print(product_dict)

def main():
    file = "all_url.txt"
    fetching_ingredient(file)

if __name__ == '__main__':
    main()