import os
from time import sleep
from behave import *
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains


@given('I am on the login page')
def step_impl(context):
    context.browser.get('https://user.itaka.pl/')
    context.browser.implicitly_wait(10)
    try:
        context.browser.find_element(by='xpath', value="//button[@data-cky-tag='accept-button']").click()
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
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

@when('I press the logout button')
def step_impl(context):
    logout = context.browser.find_element(by='css selector', value="a[class='user-login-panel-trigger'] span")
    action = ActionChains(context.browser)
    action.move_to_element(logout).perform()
    context.browser.find_element(by='xpath', value="//span[normalize-space()='Wyloguj']").click()

@then('I should see error messages')
def step_impl(context):
    list_of_warnings = context.browser.find_elements(by='css selector', value="li[class='parsley-required']")
    assert len(list_of_warnings) == 2

@then('I should see the login page')
def step_impl(context):
    title = context.browser.title
    assert title == 'Itaka.pl - Logowanie'
