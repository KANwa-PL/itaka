from behave import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@fixture
def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    context.browser = webdriver.Chrome(options=chrome_options)


# def after_all(context):
#     context.browser.close()
