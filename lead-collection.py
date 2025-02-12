from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/?hl=en")
time.sleep(10)
driver.refresh()
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Laptop shop near dhanmondi")
search_box.send_keys(Keys.RETURN)
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div[1]/div[1]/div/div[2]/a').click()

time.sleep(10)
driver.quit()