from selenium.webdriver.common.by import By


def test_panda(browser):
    browser.get("https://plugins.jenkins.io/shiningpanda")
    title_element = browser.find_element(By.XPATH, "//*[@class='title']")
    assert title_element.text == "ShiningPanda"