import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


@pytest.mark.selenium
def test_selenium_web_open_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url


# Убрал проверку для названия вкладки, потому что на GitHub он меняется
@pytest.mark.selenium
def test_selenium_web_open_github(driver):
    url = "https://github.com/"
    driver.get(url)
    assert driver.current_url == url
