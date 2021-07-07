from concurrent.futures import ThreadPoolExecutor, wait
  
values = [3,4,5,6]
  
def cube(x):
    print(f'Cube of {x}:{x*x*x}')
  
def simple_add(*args, **kwargs):
    print(args)
    a = args[0]
    b = args[1]
    print(f'sum of {a} + {b} = {a + b}')

if __name__ == '__main__':
    # style 1
    result =[]
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(cube,2)
          
        # Maps the method 'cube' with a list of values.
        result = exe.map(cube,values)
      
    for r in result:
      print(r)
    
    # style 2
    executor = ThreadPoolExecutor(max_workers=2)
    work = executor.submit(simple_add, 4, 2)
    print(work)
    print(work.result())
    print(work)


