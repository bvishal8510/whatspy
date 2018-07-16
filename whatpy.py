from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from threading import Timer

x=datetime.today()
print("x",x)
# y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
y=x.replace(day=x.day, hour=0, minute=0, second=5, microsecond=0)
print("y",y)
delta_t=y-x
print("delta_t",delta_t)
start_time = datetime.now()

driver = webdriver.Chrome('/home/vishal/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)

secs=delta_t.seconds+1
print("secs",secs)

def send_message():
	target = '"Varsha"'
	string = "Hi!!!!"
	x_arg = '//span[contains(@title,' + target + ')]'

	# try:
	# 	group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg)))
	# except:
	# 	end_time = datetime.now()
	# 	print("Time1 =", end_time - start_time)
	group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg)))
	end_time = datetime.now()
	print("Time =", end_time - start_time)
	print("after wait")
	group_title.click()
	print("1")
	inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@dir="ltr"][@data-tab="1"][@contenteditable="true"][@spellcheck="true"]'
	print("2")
	input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))
	print("3")
	input_box.send_keys(string + Keys.ENTER)
	print("4")
# for i in range(2):
# 	input_box.send_keys(string + Keys.ENTER)
# 	time.sleep(1)

# t = Timer(secs, send_message)
t = Timer(secs, send_message)
t.start()