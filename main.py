from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
import random

INSTA_USERNAME = "nom_notess"
INSTA_EMAIL = "geaa00643@gmail.com"
INSTA_PASSWORD = "x3hYf'tf-tQ:F2B"
SIMILAR_ACCOUNT = "chefsteps"

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_opts)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTA_EMAIL)

        sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTA_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        # When a prompt about saving account info pops up after log in, reject in this case
        sleep(7)
        save_info_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info_prompt:
            save_info_prompt.click()

        # When a notification prompt pops up (to allow notifications), reject in this case
        sleep(7)
        notifications_prompt = self.driver.find_element(By.XPATH, "// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        sleep(7)
        followers = self.driver.find_element(By.XPATH, "//a[contains(text(), 'followers')]")
        followers.click()

        sleep(10)
        for n in range(2, 10):
            follow_button = self.driver.find_element(By.XPATH, f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{n}]/div/div/div/div[3]/div/button/div/div")
            follow_button.click()
            sleep(random.randint(2,5))

        # Need to check if we already follow that person bcs we are going to have a popup we need to get rid of
    def follow(self):
        pass


follow_bot = InstaFollower()
follow_bot.login()
follow_bot.find_followers()
follow_bot.follow()


# To try and scroll through the list of followers
# def scroll_followers_list():
#     followers_popup = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
#     last_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)
#
#     while True:
#         driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
#         time.sleep(2)  # Adjust time as necessary
#         new_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)
#
#         if new_height == last_height:
#             break
#
#         last_height = new_height