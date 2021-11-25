time = input().split()

finish = len(time) // 2
car_left = time[0:finish]
car_right = time[:finish:-1]
left_time = 0
right_time = 0

for i in car_left:
    if int(i) == 0:
        left_time *= 0.8
    else:
        left_time += int(i)

for j in car_right:
    if int(j) == 0:
        right_time *= 0.8
    else:
        right_time += int(j)

if right_time > left_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")