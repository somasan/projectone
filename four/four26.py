from pyrob.api import *


@task
def task_2_4():

            def trem():
                fill_cell()
                for i in range(2):
                   move_down()
                   fill_cell()
                move_up()
                move_right()
                fill_cell()
                move_left(2)
                fill_cell()
                move_up()
            move_right()
            for j in range(5):
                for i in range(9):
                    trem()
                    move_right(5)
                trem()
                if j != 4:
                   move_down(4)
                   move_left(35)
            move_left(36)




if __name__ == '__main__':
    run_tasks()