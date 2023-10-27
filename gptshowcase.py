from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()


def search_for_profiles(driver, keyword):
    search_box = driver.find_element(
        By.CSS_SELECTOR, "input[type='text'][aria-label='Search']"
    )
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)


def navigate_to_profiles_and_invite(driver):
    profile_cards = driver.find_elements(By.CLASS_NAME, "entity-result__item")
    for card in profile_cards:
        try:
            card.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".pv-s-profile-actions")
                )
            )
            invite_button = driver.find_element(
                By.CSS_SELECTOR, ".pv-s-profile-actions"
            )
            invite_button.click()
            driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary").click()
        except:
            pass

        driver.back()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login_to_linkedin(driver, "freed4catalonia@gmail.com", "canadaconan17")
    time.sleep(2)

    search_for_profiles(driver, "Software Developer")
    time.sleep(2)

    navigate_to_profiles_and_invite(driver)
    driver.quit()
