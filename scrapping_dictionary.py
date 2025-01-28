# TASK 2
# STORE LINK ACCORDING TO PAGE NUMBER
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
store_product_link = {}
for i in range (1,3):
    page_type = str(i)
    driver.get('https://www.daraz.com.bd/catalog/?page='+page_type+'&q=router&spm=a2a0e.tm80335411.search.d_go')
    driver.maximize_window()
    store_link = []
    for j in range(1,4):
        change_type = str(j)
        link = driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+change_type+') > div > div > div.ICdUp > div > a')
        store_link.append(link.get_attribute('href'))
    store_product_link['Page-'+str(i)+''] = store_link
