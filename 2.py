import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://www.baidu.com/')
driver.find_element(By.XPATH,"//*[@id='s-top-left']/a[6]").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(4)
driver.close()
driver.switch_to.window(windows[0])


time.sleep(400)
