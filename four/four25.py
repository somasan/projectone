from pyrob.api import *


@task
def task_2_2():

            def trem():
                for i in range(3):
                   move_down()
                   fill_cell()
                move_up()
                move_right()
                fill_cell()
                move_left(2)
                fill_cell()
                move_up()
            move_right()
            for i in range(4):
                trem()
                move_up()
                move_right(5)
            trem()




if __name__ == '__main__':
    run_tasks()