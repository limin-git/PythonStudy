
__metaclass__ = type

import concurrent.futures

def foo():
    print 'hello, world'

pool = concurrent.futures.ThreadPoolExecutor()
pool.submit(foo)





if __name__ == '__main__':
    pass

