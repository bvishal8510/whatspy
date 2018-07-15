from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/home/vishal/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)
target = '"Varsha"'

string = "This Message was sent using a Python script!"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg)))
print("after wait")
group_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"][@contenteditable="true"][@spellcheck="true"]'
input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))
# input_box.send_keys(string + Keys.ENTER)
for i in range(2):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)