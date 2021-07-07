import time
from behave import given, then

@given('run test 4')
def run_test_4(context):
    time.sleep(2)
    pass

@then('test 4 will run')
def verify_test_4(context):
    pass