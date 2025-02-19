''' Web navigator'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    ''' main function '''
    firefoxdriver = webdriver.Firefox()
    firefoxdriver.maximize_window()
    firefoxdriver.get("https://dev.to")
    firefoxdriver.find_element(By.NAME, "q").send_keys("Selenium")
    firefoxdriver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(10)

    chromedriver = webdriver.Chrome()
    chromedriver.maximize_window()
    chromedriver.get("https://dev.to")
    chromedriver.find_element(By.NAME, "q").send_keys("Selenium")
    chromedriver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(10)

    edgedriver = webdriver.Edge()
    edgedriver.maximize_window()
    edgedriver.get("https://dev.to")
    edgedriver.find_element(By.NAME, "q").send_keys("Selenium")
    edgedriver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(10)

    firefoxdriver.close()
    chromedriver.close()
    edgedriver.close()


if __name__ == '__main__':
    main()
