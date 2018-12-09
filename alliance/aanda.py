import os
import time
from sheets import get_item_codes, write_to_sheet
from creds_file import get_creds, set_creds
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
start_time = time.time()

print('\nInitializing...\n')

if not os.path.isfile('creds.json'):
    creds_file = open('creds.json', 'w')
    set_creds(creds_file)

creds = get_creds(open('creds.json', 'r'))

item_codes = get_item_codes()
item_status_list = []
count = 1


# Selenium setup
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(creds['site'])

# Login page
user_name = browser.find_element_by_id('UserName')
password = browser.find_element_by_id('Password')
login = browser.find_element_by_id('Submit')

print('Logging in...\n')
user_name.send_keys(creds['username'])
password.send_keys(creds['password'])
login.click()
print('Searching...\n')

# Homepage
for i in item_codes:
    set_item_code = str("javascript:document.getElementsByName('itemcode')[0].value = " + "'" + i + "'" + ";")
    click_button = str("javascript:document.getElementsByName('Go')[0].click();")

    browser.execute_script(set_item_code)
    browser.execute_script(click_button)
  
    try:
        e_column = browser.find_element_by_name('E').text
        mw_column = browser.find_element_by_name('MW').text
        sw_column = browser.find_element_by_name('SW').text
        w_column = browser.find_element_by_name('W').text
    except Exception:
        e_column = None

    print('{}/{}\n'.format(count, len(item_codes)))

    if e_column:
        has_full_stock = e_column == 'Y' and mw_column == 'Y' and sw_column == 'Y' and w_column == 'Y'
        item_status_list.append([1 if has_full_stock else 0])
    else:
        item_status_list.append(['N/A'])
    count += 1

# Last steps
write_to_sheet(item_status_list)
elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print('Done!\n')
print('Elapsed time: {}'.format(pretty_time))
