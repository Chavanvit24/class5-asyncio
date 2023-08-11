import asyncio
import time

# ผลลัพย์ที่ได้จากการทำงาน
# Task A: Sum = 3
# task B: Computing 3+3
# Time: 2.01
# Task B: Sum = 6
# Time: 3.03 sec


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
# จำลองเวลาการทำงาน โดยหน่วงเวลา 1วินาที
# เปลี่ยน การทำงานของ sleep เป็น อะซิงโครนัส


async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'task {name}: Computing {total}+{number}')
        # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา
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
# จะทำลูปจนกว่างานทั้งหมดจะเสร็จ
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
