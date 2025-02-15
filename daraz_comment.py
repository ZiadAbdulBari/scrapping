import sys
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get('https://www.daraz.com.bd/products/mercusys-ac12-ac1200-i373299504.html?spm=a2a0e.searchlistcategory.list.22.42433d8flZeCvA')

height = driver.execute_script('return document.body.scrollHeight')


for i in range(0,height,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)


wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div')))

loop_list = []
global element
element = None
store_comments = {}
for i in range(1,6):
    wait = WebDriverWait(driver, 10)
    if(i>=4 and i<5):
        j='4'
        loop_list.append(4)
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{j}]')
    elif(i==5):
        loop_list.append(5)
        element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]')
    else:
        loop_list.append(i)
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')

    driver.execute_script("arguments[0].scrollIntoView();", element)
    all_comment = driver.find_elements(By.CLASS_NAME,'content')
    comment_list=[]
    for index,comment in enumerate(all_comment):
        if not index==0:
            comment_list.append(comment.text)
    store_comments[f"Page-{i}"]=comment_list
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)

print(store_comments)
time.sleep(5)
driver.quit()
