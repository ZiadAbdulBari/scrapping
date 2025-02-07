import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

root = tk.Tk()
root.geometry("300x200")
search_text = ""
def get_entry_value():
    global search_text
    search_text += input_field.get()
    root.destroy()

root.title('Google Search')
label = tk.Label(root, text='Search text')
label.pack()
input_field = tk.Entry(root)
input_field.pack()
button = tk.Button(root, text='Stop', width=25, command=get_entry_value)
button.pack()
root.mainloop()
time.sleep(10)

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.refresh()
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys(search_text)
search_box.send_keys(Keys.RETURN)
time.sleep(10)
store_web_links = []
for page in range(0,3):
    height = driver.execute_script('return document.body.scrollHeight')

    for i in range(0,height+1500,30):
        driver.execute_script(f'window.scrollTo(0,{i});')
        time.sleep(0.5)
    
    web_links = driver.find_elements(By.CSS_SELECTOR, '[jsname="UWckNb"]')
    time.sleep(5)
    for j in web_links:
        link = j.get_attribute('href')
        store_web_links.append(link)
    next_btn = driver.find_element(By.XPATH,'//*[@id="pnnext"]')
    time.sleep(0.5)
    next_btn.click()
driver.quit()
root = tk.Tk()
columns = ("Web Links")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)
table.heading(0, text='Web Links')
table.column(0, width=200)
for row in store_web_links:
    table.insert("", tk.END, values=row)
table.pack(pady=20)
root.mainloop()

