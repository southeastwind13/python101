from functools import wraps
from time import sleep


'''

'''

def retry(retries=3, delay_time=1):

    if retries < 1:
        raise ValueError("Number of retries should greater than one.")
    
    if delay_time <= 0:
        raise ValueError("Delay time should greater than or equal zero.")

    def inner(func:callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> callable:

            for i in range(1, retries+1):
                
                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:

                    if i == retries:
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        sleep(delay_time)  # Add a delay before running the next iteration
        return wrapper
    return inner
    

@retry(retries=3, delay_time=1)
def connect() -> None:
    sleep(1)
    raise Exception('Could not connect to internet...')


connect()