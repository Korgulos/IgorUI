import random
from datetime import datetime, timedelta

for i in range(9):
    d = random.randint(1, 5)

    # 👇️ convert string to datetime object
    dt = datetime.now()
    result = dt + timedelta(seconds=d)

    while True:
        if datetime.now() > result:
            break

    print(dt)  # 👉️ 2023-11-24 09:30:00.000123
    print(f"{result} more {d} seconds")
