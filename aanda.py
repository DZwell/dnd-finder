import os
from spreadsheet import get_item_codes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


item_codes = get_item_codes()

chrome_options = Options()
# chrome_options.add_argument("--headless")
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
for i in item_codes:
  set_item_code = str("javascript:document.getElementsByName('itemcode')[0].value = " + "'" + i + "'" + ";")
  click_button = str("javascript:document.getElementsByName('Go')[0].click();")

  browser.execute_script(set_item_code)
  browser.execute_script(click_button)
  # browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
  browser.execute_script('window.open("' + os.environ['SITE'] + '","_blank");')


  # Search for less than four Ys
  # 
