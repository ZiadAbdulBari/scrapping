# TASK 1
# GET LINK BY CSS SELECTOR
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/catalog/?spm=a2a0e.tm80335411.search.d_go&q=router')
driver.maximize_window()
store_link = []

for i in range (1,10):
    change_type = str(i)
    link = driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+change_type+') > div > div > div.ICdUp > div > a')
    store_link.append(link.get_attribute('href'))
print(store_link)
driver.quit()

        
