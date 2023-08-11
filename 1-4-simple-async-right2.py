import asyncio
import time

# ผลลัพย์ที่ได้จากการทำงาน
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)


async def sum(name, numbers):
    total = 0
    for number in numbers:
        # function นี้จะเป็นการนำ Number มาบวกกัน โดยจะนำค่า มาบวกเเล้ววนลูปจนกว่าจะครบเเล้วเเสดงค่าออกมา
        print(f'Task {name}: Computing {total}+{number}')
        # ใช้เพื่อเรียกฟังก์ชัน อะซิงโครนัส await เพื่อให้ทำงานอื่นขณะที่รอ sleep ทำงาน
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')


async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))
    # ใช้เพื่อเรียกใช้ฟังก์ชัน gather เพื่อให้ sum() ให้ทำงานพร้อมกัน


# ฟังก์ชันอะซิงโครนัสหลักที่เราจะใช้
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
