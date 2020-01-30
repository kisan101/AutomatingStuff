from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.merojob.com")

search = browser.find_element_by_xpath('//*[@id="job_related:job_search"]')
search.send_keys("Python Developer")

hit_button = browser.find_element_by_xpath('//*[@id="search-button"]')
hit_button.click()


'''
Tag include

'''
#get all source code
html = browser.page_source

# HTML from `<html>`
html = driver.execute_script("return document.documentElement.outerHTML;")

# HTML from `<body>`
html = driver.execute_script("return document.body.outerHTML;")

# HTML from element with some JavaScript
element = driver.find_element_by_css_selector("#hireme")
html = driver.execute_script("return arguments[0].outerHTML;", element)

# HTML from element with `get_attribute`
element = driver.find_element_by_css_selector("#hireme")
html = element.get_attribute('outerHTML')

"""
Tage Excludes
"""
# HTML from `<html>`
html = driver.execute_script("return document.documentElement.innerHTML;")

# HTML from `<body>`
html = driver.execute_script("return document.body.innerHTML;")

# HTML from element with some JavaScript
element = driver.find_element_by_css_selector("#hireme")
html = driver.execute_script("return arguments[0].innerHTML;", element)

# HTML from element with `get_attribute`
element = driver.find_element_by_css_selector("#hireme")
html = element.get_attribute('innerHTML')
