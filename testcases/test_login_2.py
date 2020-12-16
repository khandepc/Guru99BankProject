from selenium import webdriver

driver= webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.demo.guru99.com/V4/")
print(driver.title)

name_user_id="uid"
name_password="password"
name_login_button="btnLogin"
name_reset_button="btnReset"

driver.find_element_by_name(name_user_id).clear()
driver.find_element_by_name(name_user_id).send_keys("mngr270653")

driver.find_element_by_name(name_password)
driver.find_element_by_name(name_password).send_keys("etenAjY")

driver.find_element_by_name(name_login_button).click()

print(driver.title)

expected_title="Guru99 Bank Manager HomePage"
actual_title=driver.title
assert actual_title==expected_title

driver.close()