from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.facebook.com') # opens facbook login page

# search phone field
phone_field = driver.find_element_by_xpath('//*[@id="email"]')
# types phone number into the field
phone_field.send_keys('9803811367')

# search password field
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('yourpassword')

# find button
button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
button.click()

