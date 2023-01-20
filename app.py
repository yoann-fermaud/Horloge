import time

# input tuple use to set time
my_tuple = ()
# tuple alarm values
my_tuple_alarm = (8, 30, 0)


def input_time():
    global my_tuple
    my_tuple = tuple(map(int, [input(f"Enter {time} : ") for time in ("HH", "MM", "SS")]))


def set_alarm(new_tuple):
    if format_EU(my_tuple) == format_EU(new_tuple):
        print("\nWake up !\n")


def set_time():
    global my_tuple
    # "typecasting" tuple becomes list
    my_list = list(my_tuple)
    # increment hour
    if my_list[0] > 23:
        my_list[0] = 0
    # increment minute
    if my_list[1] > 59:
        my_list[1] = 0
        my_list[0] += 1
    # increment second
    if my_list[2] >= 59:
        my_list[2] = 0
        my_list[1] += 1
    else:
        my_list[2] += 1
        time.sleep(1)
    # "typecasting" list becomes tuple
    my_tuple = tuple(my_list)
    return my_tuple


def format_EU(new_tuple):
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


def display_alarm(new_tuple):
    print(f"Current alarm time : {format_EU(new_tuple)}")


def display_time():
    set_time()
    print(f"\rCurrent time : {format_EU(my_tuple)}", end="")


def main():
    input_time()
    display_alarm(my_tuple_alarm)
    while True:
        set_alarm(my_tuple_alarm)
        display_time()


if __name__ == '__main__':
    main()
