# Asyncio for concurrency in the execution of I/O operations or http request like tasks.

import asyncio
import time

async def prepare_tea():
    
    print('Starting to prepare tea.')
    await asyncio.sleep(2) # Simulating some prepare time
    return 'Tea prepared.'

async def prepare_snacks():
    
    print('Starting to prepare snacks.')
    await asyncio.sleep(3) # Simulating some prepare time
    return 'Snacks prepared.'

async def main():

    start = time.time()
    
    # #Individually assigning subroutines to execute concurrently using create_task 
    # tea_task = asyncio.create_task(prepare_tea())
    # snacks_task = asyncio.create_task(prepare_snacks())
    # result1 = await tea_task
    # result2 = await snacks_task

    # Batch handling concurrency of subroutines
    batch = asyncio.gather(prepare_tea(),prepare_snacks())
    result1,result2 = await batch 

    end = time.time()

    print(f'{result1}')
    print(f'{result2}')

    time_taken = end - start

    print(f'Time taken to prepare breakfast is {time_taken}')


asyncio.run(main())