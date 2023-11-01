from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def get_images_link(url:str,query:str
                  ):
     # Initialize a Selenium WebDriver 
    cservise=webdriver.ChromeService(executable_path='/home/hamed/Downloads/chromedriver/chromedriver')
    driver=webdriver.Chrome(service=cservise)
   
    # Open the website
    driver.get(url)
    
     
    element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'L2AGLb')))   
    element.click()
    input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'APjFqb')))  
    input.send_keys(query)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    
    wait = WebDriverWait(driver, 3)
    images_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'LatpMc.nPDzT.T3FoJb'))) 
    images_link.click()
    wait = WebDriverWait(driver, 10)
    div_images=WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//div[@data-ved='2ahUKEwjmn47clqKCAxU4VqQEHezoAMAQMyhOegUIARCgAg']"))) 
    links_list=[]
    for div in div_images:
       a= div.find_element(By.TAG_NAME,'a')
       div_element= a.find_element(By.TAG_NAME,'div')
       img_element=div_element.find_element(By.TAG_NAME,'img')
       img_link=img_element.get_attribute('href')
       links_list.append()
    driver.quit()
    return [query,links_list]
#get_followers(url="https://www.google.com",query='hani')
a=get_images_link(url="https://www.google.com",query='hani')
print(a)