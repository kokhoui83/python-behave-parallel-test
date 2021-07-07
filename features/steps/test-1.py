import time
from behave import given, then

@given('run test 1')
def run_test_1(context):
    time.sleep(2)
    pass

@then('test 1 will run')
def verify_test_1(context):
    pass