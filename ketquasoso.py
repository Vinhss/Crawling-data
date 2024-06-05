from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
import time
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
current_date = datetime.now()

for j in range(10):
    current_date -= timedelta(days=2)
    dtls=[]
    driver.get("https://www.thantai1.net/so-ket-qua")
    date_input = driver.find_element(By.XPATH, '//*[@id="end"]')
    date_input.clear()
    date_input.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year))
    view_button = driver.find_element(By.XPATH, '//*[@id="skq"]/form/div[3]/div/button')
    view_button.click()

    for i in range(400):
        try:
            result = driver.find_element(By.XPATH, f'//*[@id="skq"]/div/div[{i + 1}]/div[1]/table')
            result_ls = result.text.split("\n")
            text = '\n'.join(result_ls)
            print(text)
        except:
            continue
    time.sleep(10)
    
    driver.quit()
