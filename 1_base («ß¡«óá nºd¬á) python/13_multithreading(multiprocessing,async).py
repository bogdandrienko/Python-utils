import datetime
import time
import concurrent.futures


def task(name: str):
    start_time = time.perf_counter()
    print(f'Задача {name} стартовала\n')
    time.sleep(0.75)
    print(f'Задача {name} закончила работу {round(time.perf_counter() - start_time, 3)}\n')
    # return f'{name}'


# start_time = time.perf_counter()
# for i in range(1, 3+1):
#     task(name=f"задача {i}")
# print(f'Задачи закончили работы {round(time.perf_counter() - start_time, 3)}')

# start_time = time.perf_counter()
# with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
#     for i in range(1, 15+1):
#         executor.submit(task, (f"задача {i}",))
# print(f'Задачи закончили работы {round(time.perf_counter() - start_time, 3)}')


start_time = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor(max_workers=15) as executor:
    for i in range(1, 15+1):
        executor.submit(task, (f"задача {i}",))
print(f'Задачи закончили работы {round(time.perf_counter() - start_time, 3)}')


# CRON - *nix
# while(True){
#
# new_thread(file1(
#     ответит коллбэком
# ))
#
# new_thread2(file1(
#
# ))
# }


asyncio
aiohttp


#
#
#
#
#
#
# # Грузить тяжёлую картинку / html - весь сайт с интернета и записывать в файл
# # sync VS async VS threading VS multiprocessing
#
# # sync = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл, грузим картинку 2...
#
# # async = процесс 1: поток 1: грузим картинку 1, пока грузим картинку 1, начинаем грузить картинку 2, когда первая из
# # картинок загрузилась пишем эту картинку в файл, затем остальные...
#
# # threading = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл
# # процесс 1: поток 2: грузим картинку 2, пишем картинку 2 в файл
#
# # multiprocessing = процесс 1: грузим картинку 1, пишем картинку 1 в файл
# # процесс 2: грузим картинку 2, пишем картинку 2 в файл
# import time
#
# import requests
#
# import threading
#
# import multiprocessing
#
# import asyncio
# import aiohttp
#
#
# def measure_sync(func):
#     def decorator(*args, **kwargs):
#         time_start = time.perf_counter()
#         result = func(*args, **kwargs)
#         print(time.perf_counter() - time_start)
#         return result
#
#     return decorator
#
#
# @measure_sync
# def tick(secs: float):
#     print('hello!')
#     time.sleep(secs)
#     print('bye!')
#
#     return "123"
#
#
# def task(task_name: str):
#     print(f'BEGIN {task_name}\n', end='\n')
#
#     response = requests.get(
#         url="https://picsum.photos/370/250",
#         headers={
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/102.0.0.0 Safari/537.36'
#         }
#     )
#     with open(f'temp/{task_name}_image.jpg', 'wb') as file:
#         file.write(response.content)
#
#     print(f'END {task_name}\n', end='\n')
#
#
# @measure_sync
# def sync_task():
#     # task(f"sync_1")
#
#     for i in range(1, 11):
#         task(f"sync_{i}")
#
#
# @measure_sync
# def threading_task():
#     # thread = threading.Thread(target=task, args=(f"thread_1",), kwargs={})
#     # thread.start()
#     # thread.join()
#
#     thread_list = [threading.Thread(target=task, args=(f"thread_{x}",), kwargs={}) for x in range(1, 101)]
#     for thread in thread_list:
#         thread.start()
#     for thread in thread_list:
#         thread.join()
#
#
# @measure_sync
# def processing_task():
#     # process = multiprocessing.Process(target=task, args=(f"process_1",), kwargs={})
#     # process.start()
#     # process.join()
#
#     processing_list = [multiprocessing.Process(target=task, args=(f"process_{x}",), kwargs={}) for x in range(1, 101)]
#     for processing in processing_list:
#         processing.start()
#     for processing in processing_list:
#         processing.join()
#
#
# async def async_t(task_name: str):
#     print(f'BEGIN {task_name}\n', end='\n')
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get(
#                 url="https://picsum.photos/370/250",
#                 headers={
#                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                                   'Chrome/102.0.0.0 Safari/537.36'
#                 }
#         ) as response:
#             data = await response.read()
#
#     with open(f'temp/{task_name}_image.jpg', 'wb') as file:
#         file.write(data)
#
#     print(f'END {task_name}\n', end='\n')
#
#     return response
#
#
# def async_task():
#     time_start = time.perf_counter()
#
#     async def async_task_asyncio():  # корутина
#         await asyncio.gather(
#             *[async_t(f"async_{x}") for x in range(1, 101)]
#         )
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(async_task_asyncio())
#
#     print(time.perf_counter() - time_start)
#
#
# def test(thread: str):
#     print(f'Thread(process) {thread} started\n')
#
#     time.sleep(3)
#
#     print(f'Thread(process) {thread} ended\n')
#
#
# @measure_sync
# def start_test():
#     # sync
#     # for x in range(1, 4):
#     #     test(str(x))
#
#     # thread
#     # thread_1 = threading.Thread(target=test, args=(f"1",), kwargs={})
#     # thread_2 = threading.Thread(target=test, args=(f"2",), kwargs={})
#     # thread_3 = threading.Thread(target=test, args=(f"3",), kwargs={})
#     #
#     # thread_1.start()
#     # thread_2.start()
#     # thread_3.start()
#     #
#     # thread_1.join()
#     # thread_2.join()
#     # thread_3.join()
#
#     # process
#     # process_1 = multiprocessing.Process(target=test, args=(f"1",), kwargs={})
#     # process_2 = multiprocessing.Process(target=test, args=(f"2",), kwargs={})
#     # process_3 = multiprocessing.Process(target=test, args=(f"3",), kwargs={})
#     #
#     # process_1.start()
#     # process_2.start()
#     # process_3.start()
#     #
#     # process_1.join()
#     # process_2.join()
#     # process_3.join()
#
#     pass
#
#
# if __name__ == '__main__':
#     # sync_task()  # 60.3940136 # 1 поток, 1 процесс
#     # threading_task()  # 3.0885683  # N поток, 1 процесс
#     # processing_task()  # 14.199895  # N поток, N процесс
#     # async_task()  # 5.6319412  # 1 поток, 1 процесс
#
#     # start_test()
#     pass
#
# ########################################################################################
#
#
# import time
# import threading
# import multiprocessing
# import asyncio
#
# import requests
#
# from multuthead import measure_sync
#
#
# def test(thread: str):
#     print(f'Thread(process) {thread} started\n')
#     time.sleep(3)
#     print(f'Thread(process) {thread} ended\n')
#
#
# async def async_test(thread: str):
#     print(f'Thread(process) {thread} started\n')
#     await asyncio.sleep(3)
#     print(f'Thread(process) {thread} ended\n')
#
#
# @measure_sync
# def start_test():
#     # sync
#     # test(str('1'))
#     # test(str('2'))
#     # test(str('3'))
#
#     # thread
#     # thread_1 = threading.Thread(target=test, args=(f"1",), kwargs={})
#     # thread_2 = threading.Thread(target=test, args=(f"2",), kwargs={})
#     # thread_3 = threading.Thread(target=test, args=(f"3",), kwargs={})
#     #
#     # thread_1.start()
#     # thread_2.start()
#     # thread_3.start()
#     #
#     # thread_1.join()
#     # thread_2.join()
#     # thread_3.join()
#
#     # process
#     # process_1 = multiprocessing.Process(target=test, args=(f"1",), kwargs={})
#     # process_2 = multiprocessing.Process(target=test, args=(f"2",), kwargs={})
#     # process_3 = multiprocessing.Process(target=test, args=(f"3",), kwargs={})
#     #
#     # process_1.start()
#     # process_2.start()
#     # process_3.start()
#     #
#     # process_1.join()
#     # process_2.join()
#     # process_3.join()
#
#     # asyncio.get_event_loop().run_until_complete(
#     #     asyncio.gather(
#     #         *[async_test(str('1')), async_test(str('2')), async_test(str('3'))]
#     #     )
#     # )
#
#     pass
#
#
# def mes(func):
#     def wrap(*args, **kwargs):
#         # kwargs["value"] = kwargs["value"] // 2
#
#         # args (10, 5, 6)
#         # args[0] 10
#         # args[0]//2 5
#         # args[1:] (5, 6)
#         # (args[0]//2, args[1:],) (5, 5, 6)
#         args = (args[0] // 2, args[1:],)
#         #
#         # перехват данных до
#         #
#
#         result = func(*args, **kwargs)
#
#         #
#         # обработка данных после
#         #
#
#         # page = 2
#         # limit = 3
#         #
#         # [["1", "2", "3"], ["4", "5", "6"], ["7", "7"]]
#         # ["4", "5", "6"]
#
#         # for i in result:
#         #     print(f"record= " + str(result.index(i)+1))
#         #     print(f"page= " + str(result.index(i) // 10 + 1))
#
#         return result
#
#     return wrap
#
#
# @mes
# def get_data(value=6, val2=1, val3=1):
#     print(value)
#     url = 'https://jsonplaceholder.typicode.com/todos/'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(
#         url=url,
#         headers=headers
#     )
#     print(response.json(), '\n')
#     return response.json()
#
#
# if __name__ == '__main__':
#     time1 = time.perf_counter()
#     # start_test()
#     # res1 = get_data(value=4)
#
#     thread1 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread1.start()
#
#     thread2 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread2.start()
#
#     thread3 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread3.start()
#
#     thread4 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread4.start()
#
#     thread5 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread5.start()
#
#     thread6 = threading.Thread(target=get_data, args=(10, 5, 6))
#     thread6.start()
#
#     res1 = get_data(10, 5, 6)
#     res2 = get_data(10, 5, 6)
#     res3 = get_data(10, 5, 6)
#     res4 = get_data(10, 5, 6)
#     res5 = get_data(10, 5, 6)
#     res6 = get_data(10, 5, 6)
#
#     thread1.join()
#     thread2.join()
#     thread3.join()
#     thread4.join()
#     thread5.join()
#     thread6.join()
#
#     print(time.perf_counter() - time1)
#
# ##########################################################################
#
# import asyncio
# import multiprocessing
# import threading
# import time
# import datetime
# import concurrent.futures
# import requests
# import aiohttp
# import aiofiles
#
#
# def decorator_time_measuring(function):  # ссылка на функцию
#
#     def decorator(*args, **kwargs):
#         time_start = datetime.datetime.now()
#         print('before')
#
#         result = function(*args, **kwargs)  # вызов функции из ссылки
#
#         print('after')
#         time_stop = datetime.datetime.now()
#
#         print(time_stop - time_start)
#         return result
#
#     return decorator
#
#
# def read_ints(path):
#     lst = []
#     with open(path, 'r') as file:
#         while line := file.readline():
#             lst.append(int(line))
#     return lst
#
#
# def count_sum(ints, thread_name):
#     print(f"start thread: {thread_name}")
#
#     n = len(ints) // 2
#     counter = 0
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if ints[i] + ints[j] + ints[k] == 0:
#                     counter += 1
#                     print(f'Found in {thread_name}! Total: {counter}\n')
#     print(f"end thread: {thread_name}, counter: {counter}")
#
#
# @decorator_time_measuring
# def run_parallel(ints):
#     t1 = threading.Thread(target=count_sum, daemon=True, args=(ints, 't1'))
#     t2 = threading.Thread(target=count_sum, daemon=True, args=(ints, 't2'))
#
#     t1.start()
#     t2.start()
#
#     print('ожидание потоков')
#
#     t1.join()  # дождаться завершения потока, т.е. не завершать главную функцию
#     t2.join()  # дождаться завершения потока, т.е. не завершать главную функцию
#
#
# @decorator_time_measuring
# def run_sync(ints):
#     count_sum(ints, 'main')
#     count_sum(ints, 'main')
#
#
# @decorator_time_measuring
# def div(divisor, limit):
#     print(f'start: {divisor}\n', end='\n')
#
#     count = 0
#     for x in range(1, limit):
#         if x % divisor == 0:
#             print(f'divisor {divisor}, x = {x}\n', end='\n')
#             count += 1
#         time.sleep(0.2)
#     print(f'end {divisor}\n', end='\n')
#     return count
#
#
# @decorator_time_measuring
# def threads():
#     # div(3, 25)
#     # div(3, 25)
#     # div(3, 25)
#
#     # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     #     executor.submit(div, 3, 25)
#     #     executor.submit(div, 3, 25)
#     #     executor.submit(div, 3, 25)
#     #
#     #     print('in with\n')
#
#     with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
#         futures = []
#         for i in range(1, 4):
#             future = executor.submit(div, 3, 25)
#             futures.append(future.result())
#
#         print('in with\n')
#     #
#     # print('out with\n')
#
#
# # if __name__ == '__main__':
# # print('start main')
# #
# # ints = read_ints('random_numbers.txt')
# #
# # run_parallel(ints)
# # run_sync(ints)
# #
# # print('end main')
#
# # threads()
#
# # Грузить тяжёлую картинку / html - весь сайт с интернета и записывать в файл
# # sync VS async VS threading VS multiprocessing
#
# # sync = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл, грузим картинку 2...
#
# # async = процесс 1: поток 1: грузим картинку 1, пока грузим картинку 1, начинаем грузить картинку 2, когда первая из
# # картинок загрузилась пишем эту картинку в файл, затем остальные...
#
# # threading = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл
# # процесс 1: поток 2: грузим картинку 2, пишем картинку 2 в файл
#
# # multiprocessing = процесс 1: грузим картинку 1, пишем картинку 1 в файл
# # процесс 2: грузим картинку 2, пишем картинку 2 в файл
#
# def measuring_time(function):
#     def decorator(*args, **kwargs):
#         time_start = time.perf_counter()
#         result = function(*args, **kwargs)
#         print(function, time.perf_counter() - time_start)
#         return result
#
#     return decorator
#
#
# def task(task_name: str):
#     print(f'BEGIN {task_name}', flush=True, end='\n')
#
#     url = "https://picsum.photos/370/250"
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers)
#     with open(f'temp/{task_name}_image.jpg', 'wb') as file:
#         file.write(response.content)
#
#     print(f'END {task_name}', flush=True, end='\n')
#     return response
#
#
# async def task_async(task_name: str):
#     print(f'BEGIN {task_name}', flush=True, end='\n')
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://picsum.photos/370/250") as response:
#             data = await response.read()
#     with open(f'temp/{task_name}_image.jpg', 'wb') as file:
#         file.write(data)
#
#     print(f'END {task_name}', flush=True, end='\n')
#     return response
#
#
# @measuring_time
# def sync_tasks():
#     # start sync
#     # task('sync_1')
#
#     sync_list = [f'sync_{x}' for x in range(1, 11)]
#     for sync in sync_list:
#         task(sync)
#
#
# def async_tasks():
#     time_start = time.perf_counter()
#
#     # start async
#     # async def async_tasks_start():
#     #     await asyncio.gather(task_async(f'async_1'))
#     # asyncio.get_event_loop().run_until_complete(async_tasks_start())
#
#     async def async_tasks_start():
#         await asyncio.gather(
#             *[task_async(f'async_{x}') for x in range(1, 11)]
#         )
#
#     asyncio.get_event_loop().run_until_complete(async_tasks_start())
#
#     print('async', time.perf_counter() - time_start)
#
#
# @measuring_time
# def threading_tasks():
#     # # define thread
#     # thread_1 = threading.Thread(target=task, args=('thread_1',), kwargs={})
#     # thread_2 = threading.Thread(target=task, args=('thread_2',), kwargs={})
#     # # start thread
#     # thread_1.start()  # start the task in a new thread
#     # thread_2.start()  # start the task in a new thread
#     # # join thread
#     # thread_1.join()  # wait for the task to complete
#     # thread_2.join()  # wait for the task to complete
#
#     threading_list = [threading.Thread(target=task, args=(f'thread_{x}',), kwargs={}) for x in range(1, 11)]
#     for thread in threading_list:
#         thread.start()
#     for thread in threading_list:
#         thread.join()
#
#
# @measuring_time
# def process_tasks():
#     # # define processes
#     # process_1 = multiprocessing.Process(target=task, args=('process_1',), kwargs={})
#     # process_2 = multiprocessing.Process(target=task, args=('process_2',), kwargs={})
#     # # start processes
#     # process_1.start()  # start the task in a new process
#     # process_2.start()  # start the task in a new process
#     # # join processes
#     # process_1.join()  # wait for the task to complete
#     # process_2.join()  # wait for the task to complete
#     # # kill processes
#     # process_1.terminate()  # wait for the task to complete
#     # process_2.terminate()  # wait for the task to complete
#
#     process_list = [multiprocessing.Process(target=task, args=(f'process_{x}',), kwargs={}) for x in range(1, 11)]
#     for process in process_list:
#         process.start()
#     for process in process_list:
#         process.join()
#
#
# # entry point for the program
# if __name__ == '__main__':
#     # async_tasks()  # 1.3329052
#     # sync_tasks()  # 5.8510097
#     # threading_tasks()  # 1.1851449
#     # process_tasks()  # 1.1118587
#     pass
#
#
# ######################################################################
# #
# # class SyncAsyncThreadingPoolExecutorClass:
# #     class Example:
# #         @staticmethod
# #         # Синхронный код
# #         def example_sync_compute():
# #             # Начальное время
# #             start_time = time.time()
# #             print('start')
# #             # Генерация ссылок
# #             page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]
# #
# #             # Функция получения текста из ссылки
# #             def get_page_from_url(url):
# #                 try:
# #                     # Синхронная библиотека
# #                     response = requests.get(url=url, timeout=3)
# #                     value = f'{page_urls.index(url) + 1}: {response.text[0:15]}'
# #                     print(value)
# #                     return value
# #                 except Exception as error:
# #                     get_page_from_url(url=url)
# #
# #             responses_list = []
# #             # Цикл для прохода по ссылкам
# #             for page_url in page_urls:
# #                 resp = get_page_from_url(url=page_url)
# #                 responses_list.append(resp)
# #             for response_from_list in responses_list:
# #                 print(response_from_list)
# #
# #             # Финальное время
# #             print(f"Final time: {round(time.time() - start_time, 1)}")
# #             print('end')
# #
# #         @staticmethod
# #         # Acинхронный код
# #         def example_async_compute():
# #             # Начальное время
# #             start_time = time.time()
# #             print('start')
# #             # Генерация ссылок
# #             page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]
# #
# #             # Функция получения текста из ссылки
# #             async def get_page_from_url(session, url):
# #                 try:
# #                     # Асинхронная библиотека
# #                     async with session.get(url) as resp:
# #                         response = await resp.text()
# #                     value = f'{page_urls.index(url) + 1}: {response[0:15]}'
# #                     print(value)
# #                     return value
# #                 except Exception as error:
# #                     await get_page_from_url(session=session, url=url)
# #
# #             # Цикл для прохода по ссылкам
# #             async def main():
# #                 # Асинхронная библиотека
# #                 async with aiohttp.ClientSession() as session:
# #                     tasks = []
# #                     for page_url in page_urls:
# #                         tasks.append(
# #                             asyncio.ensure_future(
# #                                 get_page_from_url(
# #                                     session=session,
# #                                     url=page_url
# #                                 )
# #                             )
# #                         )
# #
# #                     responses_list = await asyncio.gather(*tasks)
# #
# #                     for response_from_list in responses_list:
# #                         print(response_from_list)
# #
# #             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# #             asyncio.run(main())
# #
# #             # Финальное время
# #             print(f"Final time: {round(time.time() - start_time, 1)}")
# #             print('end')
# #
# #         @staticmethod
# #         # Многопоточный Threading код
# #         def example_threading_compute():
# #             # Начальное время
# #             start_time = time.time()
# #             print('start')
# #             # Генерация ссылок
# #             page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]
# #
# #             # Функция получения текста из ссылки
# #             def get_page_from_url(page_url):
# #                 try:
# #                     # Синхронная библиотека
# #                     response = requests.get(url=page_url, timeout=3)
# #                     value = f'{page_urls.index(page_url) + 1}: {response.text[0:15]}'
# #                     print(value)
# #                     return value
# #                 except Exception as error:
# #                     get_page_from_url(page_url=page_url)
# #
# #             # Цикл для прохода по ссылкам
# #             for url in page_urls:
# #                 threading.Thread(target=get_page_from_url, args=([url])).start()
# #
# #             # Финальное время
# #             print(f"Final time: {round(time.time() - start_time, 1)}")
# #             print('end')
# #
# #         @staticmethod
# #         # Многопоточный ThreadPoolExecutor код
# #         def example_thread_pool_executor_compute():
# #             # Начальное время
# #             start_time = time.time()
# #             print('start')
# #             # Генерация ссылок
# #             page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]
# #
# #             # Функция получения текста из ссылки
# #             def get_page_from_url(page_url):
# #                 try:
# #                     # Синхронная библиотека
# #                     response = requests.get(url=page_url, timeout=3)
# #                     value = f'{page_urls.index(page_url) + 1}: {response.text[0:15]}'
# #                     print(value)
# #                     return value
# #                 except Exception as error:
# #                     get_page_from_url(page_url=page_url)
# #
# #             # Менеджер контекста для многопотока под ThreadPoolExecutor
# #             with ThreadPoolExecutor() as executor:
# #                 futures = []
# #                 # Цикл для прохода по ссылкам
# #                 for url in page_urls:
# #                     futures.append(executor.submit(get_page_from_url, page_url=url))
# #                 for future in concurrent.futures.as_completed(futures):
# #                     print(future.result())
# #
# #             # Финальное время
# #             print(f"Final time: {round(time.time() - start_time, 1)}")
# #             print('end')
# #
# #         @staticmethod
# #         # Функция получения текста из ссылки
# #         def get_page_from_url_sync(page_url):
# #             try:
# #                 # Синхронная библиотека
# #                 response = requests.get(url=page_url, timeout=3)
# #                 value = f'{response.text[0:15]}'
# #                 print(value)
# #                 return value
# #             except Exception as error:
# #                 SyncAsyncThreadingPoolExecutorClass.Example.get_page_from_url_sync(page_url=page_url)
# #
# #         @staticmethod
# #         # Мультипоточный ProcessPoolExecutor код
# #         def example_process_pool_executor_compute():
# #             # Начальное время
# #             start_time = time.time()
# #             print('start')
# #             # Генерация ссылок
# #             page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(10)]
# #
# #             # Менеджер контекста для многопотока под ThreadPoolExecutor
# #             with ProcessPoolExecutor() as executor:
# #                 futures = []
# #                 # Цикл для прохода по ссылкам
# #                 for url in page_urls:
# #                     futures.append(executor.submit(
# #                         SyncAsyncThreadingPoolExecutorClass.Example.get_page_from_url_sync,
# #                         page_url=url
# #                     ))
# #                 for future in concurrent.futures.as_completed(futures):
# #                     print(future.result())
# #
# #             # Финальное время
# #             print(f"Final time: {round(time.time() - start_time, 1)}")
# #             print('end')
