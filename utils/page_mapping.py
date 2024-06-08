from selenium.webdriver.common.by import By

angular_practice = {
    "Name_field": [By.XPATH, """//label[normalize-space()='Name']"""],
    "Email_field": [By.XPATH, """//input[@name='email']"""],
    "Password_field": [By.XPATH, """//input[@type='password']"""],
    "checkbox": [By.XPATH, """//label[@for='exampleCheck1']"""]
}