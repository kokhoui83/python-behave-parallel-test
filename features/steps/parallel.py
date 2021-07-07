from behave import step
from behave.__main__ import main as behave_main

def feature_executor(*args):
    context = args[0]
    feature = args[1]
    scenario = args[2]
    behave_main(f'-i "{feature}" -n "{scenario}" --no-capture')

@step('Executing {feature} {scenario}')
def step_impl(context, feature, scenario):
    executor = context.threadpool['executor']
    test = executor.submit(feature_executor, context, feature, scenario)
    context.threadpool['futures'].append(test)