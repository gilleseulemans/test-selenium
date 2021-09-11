from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com')

searchBox = driver.find_elements_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys("loseerr")