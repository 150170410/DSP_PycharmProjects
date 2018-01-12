__autthor__="Debasis"


from selenium import webdriver

'''driver=webdriver.Chrome("C:\\Users\\dashd\\workspace\\com.dsp.test\\src\\main\\resources\\drivers\\chromedriver.exe")'''
driver=webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.get_screenshot_as_file('C:\\Users\\dashd\\PycharmProjects\\WebnairDSP\\Screenshots\\google.png')
print(driver.title)
driver.quit()
