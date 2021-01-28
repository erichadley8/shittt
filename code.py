import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

while True:
	executable_path = os.getcwd()+"/geckodriver"
	options = Options()
	options.headless = True
	browser = webdriver.Firefox(options=options,executable_path=executable_path)
	browser.get("http://hdjshrn.tk/")
	print(browser.page_source)
	body = browser.find_elements_by_tag_name("body")
	print(body)
	body[0].click()
	browser.switch_to.window(browser.window_handles[1])
	ad = browser.find_elements_by_tag_name("iframe")
	print(ad)
	ad[0].click()
	for tab in browser.window_handles:
		browser.switch_to.window(tab)
		browser.close()
	browser.quit()
