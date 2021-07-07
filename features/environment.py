from behave import fixture, use_fixture
from concurrent.futures import ThreadPoolExecutor, as_completed

@fixture
def create_threadpool(context):
    context.threadpool = {
        'executor': None,
        'futures': []
    }

    context.threadpool['executor'] = ThreadPoolExecutor(max_workers=5)
    yield context.threadpool['executor']

    # check result if needed
    # for future in as_completed(context.threadpool['futures']):
    #     print(future.result())
    
    # cleanup threadpool once all work is done
    context.threadpool['executor'].shutdown(wait=True)


def before_tag(context, tag):
    if tag == 'fixture.threadpool.create':
        use_fixture(create_threadpool, context)