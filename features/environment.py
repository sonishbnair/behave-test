from selenium import webdriver
from behave import *
import datetime
import socket
from influx_client import send_to_influx
total_run_time = 0
'''
Run before the test (Setup)
'''
def before_all(context):
    #context.total_run_time = 0.0
    #TOTAL_TIME_TOOK = 0

    context.driver = webdriver.Chrome(executable_path='../chromedriver')
    context.timer_login = 3
    #context.driver = webdriver.Chrome(executable_path='\\synthetics\\chromedriver_win_2_3_8.exe')

    #context.driver = webdriver.Chrome(executable_path='..chromedriver')
    context.driver.set_page_load_timeout(10)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

'''
Run after the test (Teardown)
'''
def after_all(context):
    #print context.__dict__
    context.driver.quit()

def after_step(context, step):
    global total_run_time
    total_run_time += step.duration

def before_scenario(context, scenario):
    global total_run_time
    total_run_time = 0

'''
Run this after every scenario. Call influx client to send the details.
'''
def after_scenario(context, scenario):
    global total_run_time
    #if not scenario.hook_failed:
    if not context.failed:
        scenario_details = str(scenario.name).split(' ')
        jobtype = scenario_details[0]
        target = scenario_details[1]
        sample_json = [ { 	"measurement": "selenium", 	"tags": {	"host": socket.gethostname() ,	"jobtype": jobtype ,	"target" : target 	},
                             "time": str(total_run_time-context.timer_login) ,
                        "fields": { "currenttime" : str(datetime.datetime.now()) } } ]

        print('sample_json - - ', sample_json)
        # try:
        #     send_to_influx(sample_json)
        # except Exception as err:
        #     print(err)
