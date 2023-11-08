import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from datetime import date

f = open("num.txt", 'r')
number = int(f.read()) + 1
f.close()



# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation", 'enable-logging'])

# prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
# options.add_experimental_option("prefs", prefs)EES
# options.add_argument('use-fake-ui-for-media-stream')

def launch_browser():
    service = Service(executable_path=ChromeDriverManager().install())


    driver = webdriver.Chrome(service = service)

    driver.get('https://www.instagram.com/')

    driver.implicitly_wait(5)

    usern = driver.find_element(by = By.NAME, value = "username")
     
    # sends the entered username
    usern.send_keys('WRITE YOUR USERNAME HERE')
 
    # finds the password box
    passw = driver.find_element(by = By.NAME, value = "password")
 
    # sends the entered password
    passw.send_keys('WRITE YOUR PASSWORD HERE')
 
    # sends the enter key
    passw.send_keys(Keys.RETURN)

    notn = driver.find_element(by = By.CLASS_NAME, value = "_ac8f")
 
    notn.click()

    notn2 = driver.find_element(by = By.CLASS_NAME, value = "_a9_1")
    notn2.click()

    img_src = explore_post(driver)
    if len(img_src) > 0:
        download(img_src)

def saved_posts(driver):
    driver.get('https://www.instagram.com/nscrapper/saved/all-posts/')
    # profile = driver.find_element(by = By.LINK_TEXT, value = "nscrapper")
    # profile.click()

    # saved = driver.find_element(by = By.LINK, value = "/nscrapper/saved/")
    # saved.click()
    img_src = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        posts = driver.find_elements(by = By.CLASS_NAME, value = "_aagv")
        print(len(posts))
        
        for post in posts:
            img_src.add(post.find_element(by = By.TAG_NAME, value = "img").get_attribute('src'))
        

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("Total number of images : ", len(img_src))
    return img_src

def download(img_src):
    global number
    os.chdir("C:/Users/vivek/OneDrive/Desktop/New folder/insta_post_downloader/downloded_photo/")
    
    for src in img_src:
            r = requests.get(src)
            filename = f'{number}.jpg' 
            with open(filename, 'wb') as fp:
                fp.write(r.content)
            number += 1
    print("/nDowloaded")
    with open('C:/Users/vivek/OneDrive/Desktop/New folder/instaPostDownloader/instaPostDownloader/num.txt', 'w') as n:
        n.write(str(number))

def explore_post(driver):
    driver.get('https://www.instagram.com')  # link of profile

    img_src = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while len(img_src) < 10:
        posts = driver.find_elements(by = By.CLASS_NAME, value = "_aagv")
        print(len(posts))
        
        for post in posts:
            img_src.add(post.find_element(by = By.TAG_NAME, value = "img").get_attribute('src'))
        

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("Total number of images : ", len(img_src))
    return img_src

launch_browser()
