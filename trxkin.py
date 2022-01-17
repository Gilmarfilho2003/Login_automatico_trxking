from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Firefox()

browser.get("https://trxking.xyz/login.php") 

time.sleep(10)

username = browser.find_element_by_id("email")


password = browser.find_element_by_id("password")

email.send_keys("gilmarsantosfilho3.0@gmail.com")

password.send_keys("gilmarsantosfilho3.0")
--
//*[@id="recaptchav2"]/div
--
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")

login_attempt.submit()



