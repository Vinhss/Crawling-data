from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# open chrome
# driver = webdriver.Chrome("C:\\Users\\Admin\\Desktop\\AdPython\\chromedriver.exe")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://facebook.com")
# driver.maximize_window()
# driver.find_element(By.NAME, "q").send_keys("abc")
# user_name = driver.find_element(By.NAME, "email").send_keys("abcd@gmail.com")
# password = driver.find_element(By.NAME, "pass").send_keys("123456")
# enter = driver.find_element(By.NAME,"login").send_keys(Keys.ENTER)
# fg = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten password?").click()
driver.find_element(By.XPATH,"//button[@name='login']").click()
time.sleep(50)