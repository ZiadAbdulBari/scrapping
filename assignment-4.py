# PAGE SCRAP
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.daraz.com.bd/products/uiisii-c100-super-bass-stereo-in-ear-headphone-black-i174062143-s2188497994.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Aheadphone%253Bnid%253A174062143%253Bsrc%253ALazadaMainSrp%253Brn%253Ad3e2f6a72b70248892f720f11be1a857%253Bregion%253Abd%253Bsku%253A174062143_BD%253Bprice%253A222%253Bclient%253Adesktop%253Bsupplier_id%253A700507455016%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.com.bd%252F%253Bslot%253A3%253Butlog_bucket_id%253A470687%253Basc_category_id%253A155%253Bitem_id%253A174062143%253Bsku_id%253A2188497994%253Bshop_id%253A91584%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=222&priceCompare=skuId%3A2188497994%3Bsource%3Alazada-search-voucher%3Bsn%3Ad3e2f6a72b70248892f720f11be1a857%3BoriginPrice%3A22200%3BdisplayPrice%3A22200%3BsinglePromotionId%3A50000028570108%3BsingleToolCode%3AflashSale%3BvoucherPricePlugin%3A0%3Btimestamp%3A1738250093379&ratingscore=4.430290347894323&request_id=d3e2f6a72b70248892f720f11be1a857&review=3823&sale=20299&search=1&source=search&spm=a2a0e.searchlist.list.3&stock=1')
height = driver.execute_script('return document.body.scrollHeight')
for i in range(0,height+1500,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

product_name = driver.find_element(By.XPATH,'//*[@id="module_product_title_1"]/div/div/h1')
print(product_name.text)
rating = driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a[1]')
print(rating.text.split(' ')[0])
current_price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span')
print(current_price.text.split(' ')[1])
image = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div[1]/div/img[2]')
image_link = image.get_attribute('src')
download_image = requests.get(image_link).content
with open("downloaded_image.jpg", "wb") as file:
    file.write(download_image)
all_rating = []
for i in range (1,5):
    rating_count = driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[2]/ul/li['+str(i)+']/span[2]')
    all_rating.append(rating_count.text)
print(all_rating)
overall_rating = driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]')
print(overall_rating.text)

driver.quit()
