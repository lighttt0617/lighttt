import time

def pomodoro_timer(duration, break_duration):
    print("专注时间开始！")
    for i in range(duration, 0, -1):
        print(f"剩余专注时间：{i} 分钟")
        time.sleep(60)
    
    print("专注时间结束！")
    start_break(break_duration)

def start_break(duration):
    print("休息时间开始！")
    for i in range(duration, 0, -1):
        print(f"剩余休息时间：{i} 分钟")
        time.sleep(60)
    
    print("休息时间结束！")
    restart_pomodoro()

def restart_pomodoro():
    restart = input("是否开始新的专注时间？(是/否): ")
    if restart.lower() == "是":
        duration = int(input("请输入新的专注时间（分钟）: "))
        break_duration = int(input("请输入新的休息时间（分钟）: "))
        pomodoro_timer(duration, break_duration)
    else:
        print("专注时钟已结束！")

# 设置初始专注时间和休息时间
duration = int(input("请输入专注时间（分钟）: "))
break_duration = int(input("请输入休息时间（分钟）: "))

pomodoro_timer(duration, break_duration)
