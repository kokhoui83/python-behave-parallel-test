from behave import fixture, use_fixture
from concurrent.futures import ThreadPoolExecutor, as_completed, CancelledError, TimeoutError

@fixture
def create_threadpool(context):
    context.threadpool = {
        'executor': None,
        'futures': []
    }

    context.threadpool['executor'] = ThreadPoolExecutor(max_workers=5)
    yield context.threadpool['executor']

    # check result if needed
    for future in as_completed(context.threadpool['futures']):
        try:
            result = future.result()
            print(result)
        except CancelledError as ce:
            print(ce)
        except TimeoutError as te:
            print(te)
        except Exception as e:
            print(e)
    
    # cleanup threadpool once all work is done
    try:
        context.threadpool['executor'].shutdown(wait=True)
    except RuntimeError as re:
        print(re)


def before_tag(context, tag):
    if tag == 'fixture.threadpool.create':
        use_fixture(create_threadpool, context)