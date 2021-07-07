import time
from behave import given, then

@given('run test 2')
def run_test_2(context):
    time.sleep(2)
    pass

@then('test 2 will run')
def verify_test_2(context):
    pass