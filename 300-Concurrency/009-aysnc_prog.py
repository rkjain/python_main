import asyncio
import time

'''
asyncio.get_event_loop()
loop.create_task()
loop.run_until_complete()
loop.run_forever()
asyncio.gather()
loop.run_in_executor()
loop.close()
'''

# async def print_sleep(name, duration):
#     print('Started Process: ', name)
#     await asyncio.sleep(duration)
#     print('Finished Execution: ', name)

# async def main():
#     # Tasks let you run a coroutine in an event loop; that simplifies managing the execution of several coroutines.

#     task1 = asyncio.create_task(print_sleep('process1', 5))
#     task2 = asyncio.create_task(print_sleep('process2', 15))

#     await task1
#     await task2

# asyncio.run(main())

# loop = asyncio.get_event_loop()
# task1 = loop.create_task(print_sleep('process1', 5))
# task2 = loop.create_task(print_sleep('process2', 15))

# try:
#     loop.run_until_complete(
#     asyncio.gather(task1, task2)
#     )
# finally:
#     loop.close()


async def run_async(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout = asyncio.subprocess.PIPE,
        stderr = asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

async def main():
    await asyncio.gather(
        run_async('ping -c 10 www.google.com'),
        run_async('ping -c 5 www.google.com'))

asyncio.run(main())

'''
import asyncio

print("Hello")
async def my_coro(name, duration):
    print('Started: ', name)
    await asyncio.sleep(duration)
    print('Ended: ', name)

async def main():
    taskOne = asyncio.create_task(my_coro('program1', 15 ))
    taskTwo = asyncio.create_task(my_coro('program2', 10 ))
    taskThr = asyncio.create_task(my_coro('program3', 5 ))
    await asyncio.gather(taskOne, taskTwo, taskThr)
asyncio.run(main())
print("World")
'''