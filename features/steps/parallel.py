from concurrent.futures import ThreadPoolExecutor, wait
from behave import step
from behave.__main__ import main as behave_main

executor = ThreadPoolExecutor(max_workers=5)

def feature_executor(*args):
    context = args[0]
    feature = args[1]
    scenario = args[2]
    behave_main(f'-i "{feature}" -n "{scenario}" --no-capture')

@step('Executing {feature} {scenario}')
def step_impl(context, feature, scenario):
    test = executor.submit(feature_executor, context, feature, scenario)
    # test.result()