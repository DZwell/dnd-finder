import os
from sheets import get_item_codes, write_to_sheet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


item_codes = get_item_codes()
item_status_list = []

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
for i in item_codes:
  set_item_code = str("javascript:document.getElementsByName('itemcode')[0].value = " + "'" + i + "'" + ";")
  click_button = str("javascript:document.getElementsByName('Go')[0].click();")

  browser.execute_script(set_item_code)
  browser.execute_script(click_button)

  e_column = browser.find_element_by_name('E').text
  mw_column = browser.find_element_by_name('MW').text
  sw_column =  browser.find_element_by_name('SW').text
  w_column =  browser.find_element_by_name('W').text

  print(e_column, mw_column, sw_column, w_column)

  has_full_stock = e_column == 'Y' and mw_column == 'Y' and sw_column == 'Y' and w_column == 'Y'

  item_status_list.append([1 if has_full_stock else 0])

write_to_sheet(item_status_list)
