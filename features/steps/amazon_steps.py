import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

@given('I navigate to "{target_system}" login page "{url}"')
def step_impl(context, target_system, url):
    context.target_system = target_system
    context.driver.get(url)
    time.sleep(context.timer_login)

@given(u'I search for the product "{product_name}"')
def step_impl(context, product_name):
    searchElement = context.driver.find_element_by_id('twotabsearchtextbox')
    searchElement.send_keys(product_name)
    context.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
    time.sleep(3)

@then(u'I am taken to home page of "{target_system}" with page title contains "{mcux_title_contains}"')
def step_impl(context, target_system, mcux_title_contains):
    try:
        WebDriverWait(context.driver, 20).until(EC.title_contains(mcux_title_contains))
    except Exception as err:
        print(err)
        assert False
    #time.sleep(5)
    assert True
