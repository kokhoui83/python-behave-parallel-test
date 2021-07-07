import time
from behave import given, then

@given('run test 5')
def run_test_5(context):
    time.sleep(2)
    pass

@then('test 5 will run')
def verify_test_5(context):
    pass