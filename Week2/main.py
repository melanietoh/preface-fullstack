# Setting up
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Enables double clicking
from selenium.webdriver import ActionChains

# Locates elements
from selenium.webdriver.common.by import By

# Allows the programme to sleep
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)

# Visiting the website and letting the page load
driver.get('https://www.instagram.com')
time.sleep(3)

# Logging in
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('prefacelikebot')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Qpalzm971208')
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(5)

# Searching for a user
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('prefacecoding')
time.sleep(1)

# Clicking on the top search result
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
time.sleep(3)

# Scraping for the number of posts (Remove , in larger numbers)
post_num = int(driver.find_element(By.CLASS_NAME, 'g47SY ').text.replace(',',''))

# Clicking on the most recent post
driver.find_element(By.CLASS_NAME, '_9AhH0').click()
time.sleep(2)

# Liking the photo
# driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()

# For loop to like every single post on the profile
for loop in range(1, post_num+1):
    #  First iteration
    if loop == 1:
        action = ActionChains(driver)
        action.double_click(driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'))
        time.sleep(1)
        # Clicking the next post button (right)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/button').click()
        time.sleep(2)
    else:
        action = ActionChains(driver)
        action.double_click(driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'))
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/button').click()
        time.sleep(2)