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

item_codes = get_item_codes(creds['sheet_id'])
item_status_list = []
not_available = 'N/A'
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
        status_column = browser.find_element_by_name('Status').text
    except Exception:
        e_column = None

    print('{}/{}\n'.format(count, len(item_codes)))

    if e_column:
        stock_list = [e_column, mw_column, sw_column, w_column]
        if status_column:
            stock_list.append(status_column)
        item_status_list.append(stock_list)
    else:
        item_status_list.append([not_available, not_available, not_available, not_available])
    count += 1

# Last steps
write_to_sheet(item_status_list)
elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print('Done!\n')
print('Elapsed time: {}'.format(pretty_time))
