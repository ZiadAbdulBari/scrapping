import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Create text field and button
root = tk.Tk()
root.geometry("800x600")
search_text = ""
# get the text after clicking the submit button
def get_entry_value():
    global search_text
    search_text += input_field.get()
    root.destroy()

root.title('Google Search')
label = tk.Label(root, text='Search text',font=("Helvetica", 13))
label.pack()
input_field = tk.Entry(root,width=100,font=("Helvetica", 18))
input_field.pack(padx=10, pady=10)
button = tk.Button(root, text='Submit', width=25,height=2,background = "black", fg = "white",command=get_entry_value)
button.pack()
root.mainloop()
time.sleep(5)
# Initialize the webdriver
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

# search the text
store_web_links = []
for page in range(0,3):
    height = driver.execute_script('return document.body.scrollHeight')
    for i in range(0,height+1500,30):
        driver.execute_script(f'window.scrollTo(0,{i});')
        time.sleep(0.2)
    web_links = driver.find_elements(By.CSS_SELECTOR, '[jsname="UWckNb"]')
    time.sleep(5)
    for j in web_links:
        link = j.get_attribute('href')
        store_web_links.append(link)
    next_btn = driver.find_element(By.XPATH,'//*[@id="pnnext"]')
    time.sleep(0.5)
    next_btn.click()
driver.quit()

# show the links into the table
root = tk.Tk()
columns = ("Web Links")
table = ttk.Treeview(root, columns=columns, show="headings", height=100)
table.heading(0, text='Web Links')
table.column(0, width=300)
for row in store_web_links:
    table.insert("", tk.END, values=row)
table.pack(pady=20)
root.mainloop()

