import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import multiprocessing

from get_proxy import get_proxy_list


def surf_site(proxy):
    time.sleep(random.randint(5, 27))

    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    options.add_argument(
        "--ignore-certificate-errors")
    options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=options)
    driver.get("https://genpasswd.ru")
    time.sleep(7)

    all_html = driver.find_element(By.TAG_NAME, "html")

    for i in range(10):
        all_html.send_keys(Keys.DOWN)
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="select_all"]').click()
    time.sleep(7)

    kol_sim = driver.find_element(By.XPATH, '//*[@id="id_kol_sim"]')
    kol_sim.clear()
    kol_sim.send_keys(str(random.randint(8, 12)))

    time.sleep(5)

    kol_vo = driver.find_element(By.XPATH, '//*[@id="id_kol"]')
    kol_vo.clear()
    kol_vo.send_keys(str(random.randint(10, 24)))

    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/form/div[2]/button').click()

    time.sleep(27)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    get_proxy_list()
    with open('proxy.txt') as file:
        proxy_list = [line.rstrip() for line in file]
    print(proxy_list)
    with multiprocessing.Pool(processes=4) as p:
        p.map(surf_site, proxy_list)
