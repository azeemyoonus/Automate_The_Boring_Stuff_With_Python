import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()

browser.get('https://gabrielecirulli.github.io/2048/')
htmlelem=browser.find_element_by_tag_name('html')
while True:
    htmlelem.send_keys(Keys.UP)
    htmlelem.send_keys(Keys.RIGHT)
    htmlelem.send_keys(Keys.DOWN)
    htmlelem.send_keys(Keys.LEFT)
    
