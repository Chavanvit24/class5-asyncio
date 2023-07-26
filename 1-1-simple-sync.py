# 1-1-simple-sync.py
import time

#ผลลัพธ์ที่ได้จากการทำงาน
# Task A : Computing 0 + 1
# Time: 0.00
# Task A : Computing 1 + 2
# Time: 1.00
# Task A: Sum = 3

# Task B : Computing 0 + 1
# Time: 2.00
# Task B : Computing 1 + 2
# Time: 3.01
# Task B : Computing 3 + 3
# Time: 4.01
# Task B: Sum = 6

#Time: 5.01 sec

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# สร้างชื่อ function ที่ต้องการ
# ผลรวมจะมีค่า = 0


def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name} : Computing {total} + {number}')
        sleep()
        total += number
    # เอา Number มาบวกกัน โดยจะนำค่ามาบวกแล้ววนลูปจนครบค่าจะแสดงออกมา
    print(f'Task {name}: Sum = {total}\n ')


start = time.time()
# เรียกใช้ sum function โดยที่กำหนด task และค่าจำนวน
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3])
]

# print ผลลัพธ์ค่าออกมา
end = time.time()
print(f'Time: {end-start:.2f} sec')