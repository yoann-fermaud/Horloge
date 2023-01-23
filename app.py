import time
# import keyboard # Error "Install package keyboard

# input tuple use to set time
my_tuple = ()
# tuple alarm values
my_tuple_alarm = (8, 30, 0)
# AM and PM flag for set time format
am_pm_flag = False


def input_time():
    global my_tuple
    my_tuple = tuple(map(int, [input(f"Enter {var_time} : ") for var_time in ("HH", "MM", "SS")]))


def set_alarm_24(new_tuple):
    if format_24(my_tuple) == format_24(new_tuple):
        print("\nWake up !\n")


def set_time_24():
    global my_tuple
    # "typecasting" tuple becomes list
    my_list = list(my_tuple)
    # increment second
    if my_list[2] > 59:
        my_list[2] = 0
        my_list[1] += 1
    else:
        my_list[2] += 1
        time.sleep(1)
    # increment minute
    if my_list[1] > 59:
        my_list[1] = 0
        my_list[0] += 1
    # increment hour
    if my_list[0] > 23:
        my_list[0] = 0
    # "typecasting" list becomes tuple
    my_tuple = tuple(my_list)
    return my_tuple


def set_time_12():
    global my_tuple, am_pm_flag
    # "typecasting" tuple becomes list
    my_list = list(my_tuple)
    # increment second
    if my_list[2] > 59:
        my_list[2] = 0
        my_list[1] += 1
    else:
        my_list[2] += 1
        time.sleep(1)
    # increment minute
    if my_list[1] > 59:
        my_list[1] = 0
        my_list[0] += 1
    # increment hour
    if my_list[0] > 23:
        my_list[0] = 0
    # format AM or PM
    if my_list[0] < 12:
        am_pm_flag = True
    else:
        am_pm_flag = False
    # "typecasting" list becomes tuple
    my_tuple = tuple(my_list)
    return my_tuple


def format_24(new_tuple):
    # "typecasting" tuple becomes list
    my_list = list(new_tuple)
    # format HH MM SS
    if my_list[0] < 10:
        my_list[0] = "0" + str(my_list[0])
    if my_list[1] < 10:
        my_list[1] = "0" + str(my_list[1])
    if my_list[2] < 10:
        my_list[2] = "0" + str(my_list[2])
    # "typecasting" list becomes tuple
    format_tuple = tuple(my_list)
    return str(format_tuple[0]) + ":" + str(format_tuple[1]) + ":" + str(format_tuple[2])


def format_12(new_tuple):
    global am_pm_flag
    # "typecasting" tuple becomes list
    my_list = list(new_tuple)
    # format AM or PM
    if my_list[0] == 0:
        my_list[0] = 12
        am_pm_flag = True
    # format HH MM SS
    if my_list[0] > 12:
        my_list[0] -= 12
    if my_list[0] < 10:
        my_list[0] = "0" + str(my_list[0])
    if my_list[1] < 10:
        my_list[1] = "0" + str(my_list[1])
    if my_list[2] < 10:
        my_list[2] = "0" + str(my_list[2])
    # Displaying AM or PM
    if am_pm_flag:
        # "typecasting" list becomes tuple
        format_tuple = tuple(my_list)
        return str(format_tuple[0]) + ":" + str(format_tuple[1]) + ":" + str(format_tuple[2]) + " AM"
    else:
        # "typecasting" list becomes tuple
        format_tuple = tuple(my_list)
        return str(format_tuple[0]) + ":" + str(format_tuple[1]) + ":" + str(format_tuple[2]) + " PM"


def display_alarm_24(new_tuple):
    print(f"Current alarm time : {format_24(new_tuple)}")


def display_time_24():
    set_time_24()
    print(f"\rCurrent time : {format_24(my_tuple)}", end="")


def display_time_12():
    set_time_12()
    print(f"\rCurrent time : {format_12(my_tuple)}", end="")


def main():
    input_time()
    # display_alarm_24(my_tuple_alarm)
    while True:
        # set_alarm_24(my_tuple_alarm)
        # display_time_24()
        display_time_12()


if __name__ == '__main__':
    main()
