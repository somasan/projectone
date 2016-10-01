from pyrob.api import *


@task
def task_7_5():
    a = 1
    move_right()
    fill_cell()
    while wall_is_on_the_right() == False:
        fill_cell()
        for i in range(a):
            if wall_is_on_the_right() == False:
                move_right()

        a += 1

if __name__ == '__main__':
    run_tasks()