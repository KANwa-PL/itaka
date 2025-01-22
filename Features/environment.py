from behave import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

@fixture
def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    context.browser = webdriver.Chrome(options=chrome_options)
    load_dotenv()
