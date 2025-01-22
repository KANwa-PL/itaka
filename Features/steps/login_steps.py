import os
from behave import *
from selenium.common import NoSuchElementException

@given('I am on the login page')
def step_impl(context):
    context.browser.get('https://user.itaka.pl/')
    context.browser.implicitly_wait(10)
    try:
        context.browser.find_element(by='xpath', value="//button[@data-cky-tag='accept-button']").click()
    except NoSuchElementException:
        pass
    context.browser.fullscreen_window()


@given('I fill in the username')
def step_impl(context):
    user = os.getenv('USERNAME')
    context.browser.find_element(by='name', value='_username').send_keys(user)


@given('I fill in the password')
def step_impl(context):
    password = os.getenv('PASSWORD')
    context.browser.find_element(by='name', value='_password').send_keys(password)


@when('I press the login button')
def step_impl(context):
    context.browser.find_element(by='css selector', value='button[type="submit"]').click()


@then('I am taken to client area and should see welcome message')
def step_impl(context):
    context.browser.fullscreen_window()
    title = context.browser.title
    text = context.browser.find_element(by='xpath', value="//h4[contains(text(),'Dzień dobry!')]").text

    assert text == 'Dzień dobry!' and title == 'Biuro podróży ITAKA | Strefa klienta'
