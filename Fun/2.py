from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\as200\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

# driver.get("https://www.hotstar.com/in")
# driver.find_element_by_id("searchField").send_keys("Movies")
# driver.find_element("searchField").send_keys("Movies")
# driver.find_element_by_css_selector("#searchField").send_keys("Sports")
# driver.find_element_by_partial_link_text("Premi").click()


driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("btnK").click()