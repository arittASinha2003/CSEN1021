
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.youtube.com")

##########################################

search_string = input("Input the URL or string you want to search for:")

search_string = search_string.replace(' ', '+')

# browser = webdriver.Chrome('chromedriver')

# for i in range(1):
# 	matched_elements = driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

for i in range(1):
	matched_elements = driver.get("https://www.google.com/search?q=" + search_string + "&oq=" + search_string + "&sourceid=chrome&ie=UTF-8&start=" + str(i))

##############################################

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.youtube.com")
# time.sleep(2)

# driver.close()
# driver.quit()