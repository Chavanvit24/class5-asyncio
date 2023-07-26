import asyncio
import time

# #Wed Jul 26 15:04:14 2023 hello 1 started
# Wed Jul 26 15:04:14 2023 hello 2 started
# Wed Jul 26 15:04:18 2023 hello 1 done
# Wed Jul 26 15:04:18 2023 hello 2 done
# Time: 4.01 sec

# ส่ง output เป็นวันเวลา hello start/stop
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# สร้าง main สร้าง task 2 task ใช้ gather เพื่อเขียนย่อ คล้ายกับการสร้าง list
async def main():
    task1 = asyncio.create_task(hello(1))
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

# กำหนดเวลาเริ่มต้นถึงสิ้นสุด สั่งรันค่า function main print ค่าแสดงเวลาที่ทำงานทั้งหมด
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')