import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30


def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")


# ใช้เวลาคิด 5 วินาที ฝ่ายตรงข้าม 55 วิ ดังนั้น 1 รอบ เราใช้เวลาเดิน 60 วิ
# 1 เกม ฝ่ายเราและฝั่งตรงข้าม เดินได้ 30 รอบ มีทั้งหมด 24 เกม = 60*30*24 = 43200 วินาที
# 43200/60/60 จะได้ 12 ชั่วโมง

# 100 รอบ = 60*30*100 = 50 ชั่วโมง