from pyrob.api import *


@task
def task_2_1():
             move_right(2)
             for i in range(3):
                 move_down()
                 fill_cell()
             move_up()
             move_right()
             fill_cell()
             move_left(2)
             fill_cell()
             move_up()



if __name__ == '__main__':
    run_tasks()