from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


class InstagramBot:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__driver = webdriver.Firefox()

    def __del__(self):
        self.__driver.close()

    @staticmethod
    def __print_same_line(text):
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write(text)
        sys.stdout.flush()

    def login(self):
        driver = self.__driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.__username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.__password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, tag):
        driver = self.__driver
        driver.get("https://www.instagram.com/explore/tags/" + tag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if
                                 '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath(
                    '//span[@class="glyphsSpriteHeart__outline__24__grey_9 u-__7" and @aria-label="Like"]')
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    InstagramBot.__print_same_line(
                        "#" + tag + ': unique photos left: ' + str(unique_photos) + " | Sleeping " + str(second))
                    time.sleep(1)
            except:
                time.sleep(2)
            unique_photos -= 1
