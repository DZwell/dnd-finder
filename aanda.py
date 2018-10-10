import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(os.environ['SITE'])

# Login page
user_name = browser.find_element_by_id('UserName')
password = browser.find_element_by_id('Password')
login = browser.find_element_by_id('Submit')

user_name.send_keys(os.environ['USERNAME'])
password.send_keys(os.environ['PASSWORD'])
login.click()

# Homepage
setItemCode = str("javascript:document.getElementsByName('itemcode')[0].value = 'SWF35';")
clickButton = str("javascript:document.getElementsByName('Go')[0].click();")

browser.execute_script(setItemCode)
browser.execute_script(clickButton)