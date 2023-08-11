import asyncio
import time

# ผลลัพย์ที่ได้จากการทำงาน
# task A: Computing 0+1
# Time: 0.00
# task A: Computing 1+2
# Time: 0.00
# Task A: Sum = 3

# task B: Computing 0+1
# Time: 0.00
# task B: Computing 1+2
# Time: 0.00
# task B: Computing 3+3
# Time: 0.00
# Task B: Sum = 6

# Time: 0.01 sec


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep
# จำลองเวลาการทำงาน โดยหน่วงเวลา 1วินาที

async def sum(name, numbers):
    total = 0
    for number in numbers:
        # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา 
        print(f'task {name}: Computing {total}+{number}')
        await sleep()
        # ใช้เพื่อเรียกฟังก์ชัน อะซิงโครนัส await เพื่อให้ทำงานอื่นขณะที่รอ sleep ทำงาน
        total += number
    print(f'Task {name}: Sum = {total}\n')
    

start = time.time()

loop = asyncio.get_event_loop()
# สร้างลูปเพื่อรับค่า 
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
#จะทำลูปจนกว่างานทั้งหมดจะเสร็จ 
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
