import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

# Task A: Sum = 3

# TaskB: Computing 3+3
# Task B: Sum = 6

# Time; 0.02 sec


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
    # จำลองเวลาการทำงาน โดยหน่วงเวลา 1วินาที

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    #_executor จะสร้างเธรด ที่มี 2 Task จะถูกเรียกใช้พร้อมกับ sleep
    total = 0
    for number in numbers:
         # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา
        print(f'Task{name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
         # ใช้เพื่อเรียกฟังก์ชัน อะซิงโครนัส await เพื่อให้ทำงานอื่นขณะที่รอ sleep ทำงาน
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
# สร้างลูปเพื่อรับค่า
task = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3]))
]
loop.run_until_complete(asyncio.wait(task))
#จะทำลูปจนกว่างานทั้งหมดจะเสร็จ 
loop.close()

end = time.time()
print(f'Time; {end-start:.2f} sec')
