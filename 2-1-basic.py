import asyncio
import time

#ผลลัพธ์
# Wed Jul 26 14:43:29 2023 hello 1 started
# Wed Jul 26 14:43:29 2023 hello 2 started
# Wed Jul 26 14:43:33 2023 hello 1 done
# Wed Jul 26 14:43:33 2023 hello 2 done
# Time: 4.02 sec

# ส่ง output เป็นวันเวลา hello start/stop
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้าง main สร้าง task 2 task 
async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately,  the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

# กำหนดเวลาเริ่มต้นถึงสิ้นสุด สั่งรันค่า function main print ค่าแสดงเวลาที่ทำงานทั้งหมด
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')