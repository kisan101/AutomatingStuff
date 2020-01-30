from selenium import webdriver
from selenium.webdriver.common.keys import Keys
window = webdriver.Chrome()

window.get('https://www.facebook.com/messages/t/2978728965474130')
window.find_element_by_xpath('//*[@id="placeholder-rc2j"]')

element = driver.find_element_by_id("Value")
element.send_keys("keysToSend")
element.submit()


