import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_proxy_list():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    options.add_argument(
        "--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    driver.get("http://free-proxy.cz/ru/proxylist/country/all/http/ping/level1")

    time.sleep(3)

    with open('proxy.txt', 'w') as f:
        for r in range(1, 5):
            host = driver.find_element(By.XPATH, f'//*[@id="proxy_list"]/tbody/tr[{str(r)}]/td[1]').text
            port = driver.find_element(By.XPATH, f'//*[@id="proxy_list"]/tbody/tr[{str(r)}]/td[2]/span').text
            f.write(f'{host}:{port}\n')
        for r in range(6, 16):
            host = driver.find_element(By.XPATH, f'//*[@id="proxy_list"]/tbody/tr[{str(r)}]/td[1]').text
            port = driver.find_element(By.XPATH, f'//*[@id="proxy_list"]/tbody/tr[{str(r)}]/td[2]/span').text
            f.write(f'{host}:{port}\n')

