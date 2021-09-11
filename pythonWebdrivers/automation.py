from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys('loser')

searchKey = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchKey.click()

linkButton = driver.find_element_by_xpath('//*[@id="rso"]/div[5]/div/div[1]/a/h3')
linkButton.click()





