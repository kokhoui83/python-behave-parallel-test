import time
from behave import given, then

@given('run test 3')
def run_test_3(context):
    time.sleep(2)
    pass

@then('test 3 will run')
def verify_test_3(context):
    pass