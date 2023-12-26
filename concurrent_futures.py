import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(do_something, 1)
    print(future.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds')
