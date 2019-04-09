# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QqSpider(object):
    def __init__(self, usr, passwd):
        self.usr = usr
        self.passwd = passwd
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def run(self):
        self.driver.get('https://im.qq.com/')
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login"]'))
            ).click()

            self.driver.switch_to.frame('login_frame')
            element = self.driver.find_element_by_id('switcher_plogin')
            element.click()

            usr_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="u"]'))
            )
            usr_element.clear()
            usr_element.send_keys(self.usr)

            self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="p"]'))
            ).send_keys(self.passwd)

            self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login_button"]'))
            ).click()

        except Exception:
            self.driver.quit()
            print('FAIL!!!')


if __name__ == '__main__':
    usr = input('usr:')
    passwd = input('passwd:')

    spider = QqSpider(usr, passwd)
    spider.run()
