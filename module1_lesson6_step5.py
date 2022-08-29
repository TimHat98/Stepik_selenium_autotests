from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    input1 = browser.find_element_by_tag_name('input')
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()